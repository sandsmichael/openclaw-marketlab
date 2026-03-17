import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date

# ---------------------------
# Config
# ---------------------------
ENGINE_URI = 'postgresql://<REDACTED_USER>:<REDACTED_PASS>@<REDACTED_HOST>:5432/marketlab'
OUT_CSV = f'/home/msands/.openclaw/workspace/skills/backtest/agentic/{date.today().isoformat()}_backtest_results.csv'

np.seterr(all='ignore')

# ---------------------------
# Utilities
# ---------------------------

def annualized_stats(port_ret: pd.Series, bench_ret: pd.Series):
    x = port_ret.dropna()
    if len(x) < 252:
        return None
    b = bench_ret.reindex(x.index).dropna()
    x = x.reindex(b.index)
    if len(x) < 252:
        return None

    nav = (1 + x).cumprod()
    years = (x.index[-1] - x.index[0]).days / 365.25
    if years <= 0:
        return None

    cagr = nav.iloc[-1] ** (1 / years) - 1
    vol = x.std() * np.sqrt(252)
    sharpe = (x.mean() * 252) / (vol + 1e-12)
    downside = x[x < 0].std() * np.sqrt(252)
    sortino = (x.mean() * 252) / (downside + 1e-12)
    dd = nav / nav.cummax() - 1
    maxdd = dd.min()
    calmar = cagr / abs(maxdd) if maxdd < 0 else np.nan

    ex = x - b
    te = ex.std() * np.sqrt(252)
    ir = (ex.mean() * 252) / (te + 1e-12)
    beta = np.cov(x, b)[0, 1] / (np.var(b) + 1e-12)
    alpha = (x.mean() * 252) - beta * (b.mean() * 252)

    return {
        'start': str(x.index[0].date()),
        'end': str(x.index[-1].date()),
        'obs_days': int(len(x)),
        'CAGR': float(cagr),
        'Vol': float(vol),
        'Sharpe': float(sharpe),
        'Sortino': float(sortino),
        'MaxDD': float(maxdd),
        'Calmar': float(calmar),
        'TotalReturn': float(nav.iloc[-1] - 1),
        'WinRate': float((x > 0).mean()),
        'AnnExcessRet': float(ex.mean() * 252),
        'TrackingErr': float(te),
        'InfoRatio': float(ir),
        'Beta': float(beta),
        'Alpha': float(alpha),
    }


def zscore_series(s: pd.Series):
    m = s.mean()
    sd = s.std()
    if sd == 0 or np.isnan(sd):
        return s * 0.0
    return (s - m) / sd


def monthly_weights_from_scores(scores: pd.DataFrame, topk: int, long_lowest: bool = False, cash_filter: bool = False):
    me = scores.resample('ME').last()
    w = pd.DataFrame(0.0, index=me.index, columns=me.columns)
    for dt, row in me.iterrows():
        r = row.dropna()
        if len(r) < topk:
            continue
        r = r.sort_values(ascending=not long_lowest)
        picked = r.index[:topk]
        if cash_filter:
            best = row[picked[0]]
            if (not long_lowest and best <= 0) or (long_lowest and best >= 0):
                continue
        w.loc[dt, picked] = 1.0 / topk
    wd = w.shift(1).reindex(scores.index, method='ffill').fillna(0.0)
    return wd


def monthly_stock_long_only(scores_me: pd.DataFrame, daily_rets: pd.DataFrame, topk: int):
    w_me = pd.DataFrame(0.0, index=scores_me.index, columns=scores_me.columns)
    for dt, row in scores_me.iterrows():
        r = row.dropna().sort_values(ascending=False)
        if len(r) < topk:
            continue
        sel = r.index[:topk]
        w_me.loc[dt, sel] = 1.0 / topk
    wd = w_me.shift(1).reindex(daily_rets.index, method='ffill').fillna(0.0)
    pr = (wd * daily_rets.fillna(0.0)).sum(axis=1)
    return pr


# ---------------------------
# Data load
# ---------------------------
engine = create_engine(ENGINE_URI)

with engine.connect() as conn:
    prices = pd.read_sql(text('select date,ticker,adj_px from prices order by date'), conn)
    macro = pd.read_sql(text('select date, "VIX_LVL" as vix, "CPI_YOY" as cpi_yoy, "FEDFUNDS_LVL" as fedfunds, "GS10_LVL" as gs10, "DTB3_LVL" as dtb3 from macro order by date'), conn)
    syc = pd.read_sql(text('select date, country, yield_type, "10_yr" as y10, "2_yr" as y2, "3_mo" as y3m from sovereign_yield_curve where country=\'US\' order by date'), conn)
    fundamentals = pd.read_sql(text('select ticker, hl_pe_ratio, hl_profit_margin, hl_return_on_equity_ttm, hl_operating_margin_ttm from fundamentals'), conn)
    earn = pd.read_sql(text('select ticker, report_date, surprise_percent from earnings_history where report_date is not null'), conn)
    gspc_const = pd.read_sql(text("""
        select ticker, date
        from constituents
        where universe='GSPC.INDX'
    """), conn)

prices['date'] = pd.to_datetime(prices['date'])
px = prices.pivot(index='date', columns='ticker', values='adj_px').sort_index()
ret = px.pct_change(fill_method=None)

benchmark = ret['SPY.US'].copy() if 'SPY.US' in ret.columns else ret.mean(axis=1)

macro['date'] = pd.to_datetime(macro['date'])
macro = macro.set_index('date').sort_index()

syc['date'] = pd.to_datetime(syc['date'])
syc = syc.sort_values('date')
syc_bench = syc[syc['yield_type'] == 'benchmark'].set_index('date')[['y10', 'y2', 'y3m']]
if syc_bench.empty:
    syc_bench = syc[syc['yield_type'] == 'par'].set_index('date')[['y10', 'y2', 'y3m']]

curve = syc_bench.reindex(ret.index, method='ffill')
curve_slope = curve['y10'] - curve['y2']
curve_3m10y = curve['y10'] - curve['y3m']

# earnings trailing feature
earn['report_date'] = pd.to_datetime(earn['report_date'])
earn = earn.dropna(subset=['ticker', 'report_date'])
me_surprise = (
    earn.assign(month=lambda d: d['report_date'].dt.to_period('M').dt.to_timestamp('M'))
        .groupby(['month', 'ticker'])['surprise_percent']
        .mean()
        .unstack('ticker')
        .sort_index()
)
earn_feat_me = me_surprise.rolling(4, min_periods=1).mean()

# stock universe: latest GSPC constituents that exist in prices
gspc_const['date'] = pd.to_datetime(gspc_const['date'])
latest_const_date = gspc_const['date'].max()
stock_universe = sorted(set(gspc_const[gspc_const['date'] == latest_const_date]['ticker']) & set(px.columns))
stock_px = px[stock_universe]
stock_ret = stock_px.pct_change(fill_method=None)

# fundamentals (static snapshot as available)
fund = fundamentals.dropna(subset=['ticker']).drop_duplicates('ticker').set_index('ticker')
fund = fund.reindex(stock_universe)

# ---------------------------
# Strategy generation
# ---------------------------
rows = []

def add_result(name, description, sret):
    st = annualized_stats(sret, benchmark)
    if st is None:
        return
    rows.append({'Strategy': name, 'Description': description, **st})

# ETF universes
etf_maj = [x for x in ['SPY.US', 'IWM.US', 'EFA.US', 'EEM.US'] if x in px.columns]
etf_factor = [x for x in ['MTUM.US', 'QUAL.US', 'USMV.US', 'VLUE.US', 'SIZE.US'] if x in px.columns]
etf_style = [x for x in ['IWF.US', 'IWD.US', 'IWM.US', 'SPY.US'] if x in px.columns]
etf_all = sorted(set(etf_maj + etf_factor + etf_style))

# 1) Momentum ETF rotations
for u_name, cols in [('maj', etf_maj), ('factor', etf_factor), ('style', etf_style), ('all', etf_all)]:
    if len(cols) < 2:
        continue
    for lb in [21, 63, 126, 252]:
        score = px[cols].pct_change(lb, fill_method=None)
        for topk in [1, 2, 3]:
            if topk > len(cols):
                continue
            for cf in [False, True]:
                w = monthly_weights_from_scores(score, topk=topk, long_lowest=False, cash_filter=cf)
                pret = (w * ret[cols].fillna(0.0)).sum(axis=1)
                add_result(
                    f'ETF_MOM_{u_name}_lb{lb}_k{topk}_cf{int(cf)}',
                    f'Month-end rotation in {u_name} ETFs. Signal=trailing {lb}-day return. Long top {topk} equally weighted. Cash filter={cf}.',
                    pret
                )

# 2) Macro+Treasury regime ETF switches
vix = macro['vix'].reindex(ret.index, method='ffill')
cpi = macro['cpi_yoy'].reindex(ret.index, method='ffill')
fed = macro['fedfunds'].reindex(ret.index, method='ffill')

pairs = [(a, b) for a, b in [('IWF.US', 'USMV.US'), ('MTUM.US', 'USMV.US'), ('SPY.US', 'USMV.US'), ('IWM.US', 'SPY.US')] if a in ret.columns and b in ret.columns]

for th in [14, 16, 18, 20, 22]:
    sig = (vix < th).astype(float).shift(1).fillna(0.0)
    for a, b in pairs:
        pret = sig * ret[a].fillna(0.0) + (1 - sig) * ret[b].fillna(0.0)
        add_result(
            f'ETF_VIXSWITCH_{th}_{a}_{b}',
            f'Daily regime switch: if VIX<{th} hold {a}, else {b}. 1-day lag.',
            pret
        )

for th in [-1.0, -0.5, 0.0, 0.5]:
    sig = (curve_slope > th).astype(float).shift(1).fillna(0.0)
    for a, b in pairs:
        pret = sig * ret[a].fillna(0.0) + (1 - sig) * ret[b].fillna(0.0)
        add_result(
            f'ETF_CURVESWITCH_{th}_{a}_{b}',
            f'Daily treasury-curve regime: if (10Y-2Y)>{th} hold {a}, else {b}. 1-day lag.',
            pret
        )

for cpi_th in [2.0, 3.0, 4.0]:
    for slope_th in [-0.5, 0.0]:
        sig = ((cpi > cpi_th) & (curve_3m10y > slope_th) & (fed < 5.0)).astype(float).shift(1).fillna(0.0)
        if 'MTUM.US' in ret.columns and 'USMV.US' in ret.columns:
            pret = sig * ret['MTUM.US'].fillna(0.0) + (1 - sig) * ret['USMV.US'].fillna(0.0)
            add_result(
                f'ETF_MACRO_BLEND_cpi{cpi_th}_sl{slope_th}',
                f'Macro blend: risk-on when CPI_YOY>{cpi_th}, 10Y-3M>{slope_th}, FedFunds<5; hold MTUM else USMV. 1-day lag.',
                pret
            )

# 3) Earnings-informed ETF factor timing (using constituent earnings breadth proxy)
if len(stock_universe) > 0:
    earn_me = earn_feat_me.reindex(columns=stock_universe)
    breadth = (earn_me > 0).mean(axis=1)
    breadth = breadth.reindex(ret.index, method='ffill')
    for th in [0.50, 0.55, 0.60]:
        if 'IWF.US' in ret.columns and 'IWD.US' in ret.columns:
            sig = (breadth > th).astype(float).shift(1).fillna(0.0)
            pret = sig * ret['IWF.US'].fillna(0.0) + (1 - sig) * ret['IWD.US'].fillna(0.0)
            add_result(
                f'ETF_EARN_BREADTH_{th}',
                f'Earnings breadth proxy from S&P500 constituents: fraction with trailing 4Q avg surprise>0. If breadth>{th}, hold IWF else IWD.',
                pret
            )

# 4) Stock-level cross-sectional strategies (required)
stock_me = stock_px.resample('ME').last()
stock_mom1 = stock_me.pct_change(1)
stock_mom3 = stock_me.pct_change(3)
stock_mom6 = stock_me.pct_change(6)
stock_mr1 = -stock_mom1

earn_me_stock = earn_feat_me.reindex(stock_me.index, method='ffill').reindex(columns=stock_universe)

pe = fund['hl_pe_ratio']
roe = fund['hl_return_on_equity_ttm']
pm = fund['hl_profit_margin']
opm = fund['hl_operating_margin_ttm']

# Fundamental static cross-sectional z-scores
z_val = -zscore_series(pe.replace([np.inf, -np.inf], np.nan))
z_qual = zscore_series(roe) + zscore_series(pm) + zscore_series(opm)

for topk in [20, 30, 50, 75]:
    # pure momentum
    for lb, mom in [(3, stock_mom3), (6, stock_mom6)]:
        score = mom.copy()
        pret = monthly_stock_long_only(score, stock_ret, topk)
        add_result(
            f'STOCK_MOM_lb{lb}_k{topk}',
            f'Stock-level monthly cross-sectional momentum over {lb} months in latest S&P500 members; long top {topk} equal-weight.',
            pret
        )

    # value-quality blend
    for wm, wv, wq in [(0.5, 0.25, 0.25), (0.4, 0.3, 0.3), (0.33, 0.33, 0.34)]:
        score = wm * stock_mom6 + wv * z_val + wq * z_qual
        pret = monthly_stock_long_only(score, stock_ret, topk)
        add_result(
            f'STOCK_MOM_VAL_QUAL_k{topk}_w{wm}_{wv}_{wq}',
            f'Stock-level composite score = {wm}*6M momentum + {wv}*value(z of -PE) + {wq}*quality(z of ROE/profit/operating margins); long top {topk}.',
            pret
        )

    # earnings + momentum
    for we, wm in [(0.5, 0.5), (0.6, 0.4), (0.4, 0.6)]:
        score = we * earn_me_stock + wm * stock_mom3
        pret = monthly_stock_long_only(score, stock_ret, topk)
        add_result(
            f'STOCK_EARN_MOM_k{topk}_w{we}_{wm}',
            f'Stock-level score = {we}*trailing-4Q avg earnings surprise + {wm}*3M momentum; long top {topk}.',
            pret
        )

    # macro-conditioned stock portfolio: risk-off tilts to quality, risk-on to momentum
    risk_on = ((curve_slope.reindex(stock_me.index, method='ffill') > 0) & (vix.reindex(stock_me.index, method='ffill') < 20)).astype(float)
    score_on = stock_mom6
    score_off = z_qual.to_frame().T.reindex(stock_me.index).reindex(columns=stock_universe)
    score = risk_on.values.reshape(-1, 1) * score_on + (1 - risk_on.values.reshape(-1, 1)) * score_off
    pret = monthly_stock_long_only(score, stock_ret, topk)
    add_result(
        f'STOCK_MACRO_MOM_QUAL_k{topk}',
        f'Macro-conditioned stock strategy: if (10Y-2Y>0 and VIX<20) rank by 6M momentum, else rank by quality z-score; long top {topk}.',
        pret
    )

    # short-term reversal + quality
    score = 0.6 * stock_mr1 + 0.4 * z_qual
    pret = monthly_stock_long_only(score, stock_ret, topk)
    add_result(
        f'STOCK_REV_QUAL_k{topk}',
        f'Stock-level mean-reversion blend: score = 0.6*(-1M momentum) + 0.4*quality z-score; long top {topk}.',
        pret
    )

# 5) ETF MA-trend family (technical breadth)
for t in etf_all:
    for f, s in [(20, 100), (20, 200), (50, 200), (100, 200)]:
        ma_f = px[t].rolling(f).mean()
        ma_s = px[t].rolling(s).mean()
        sig = (ma_f > ma_s).astype(float).shift(1).fillna(0.0)
        pret = sig * ret[t].fillna(0.0)
        add_result(
            f'ETF_TREND_{t}_{f}_{s}',
            f'Trend-following: long {t} when MA{f}>MA{s}, else cash.',
            pret
        )

# ---------------------------
# Save
# ---------------------------
results = pd.DataFrame(rows)
if results.empty:
    raise RuntimeError('No valid strategies produced.')

results = results.sort_values(['InfoRatio', 'Sharpe', 'CAGR'], ascending=[False, False, False]).reset_index(drop=True)
results.to_csv(OUT_CSV, index=False)

print(f'WROTE {OUT_CSV}')
print(f'STRATEGIES {len(results)}')
print(results[['Strategy', 'InfoRatio', 'Sharpe', 'CAGR', 'AnnExcessRet', 'MaxDD']].head(20).to_string(index=False))