import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date

ENGINE_URI = os.getenv('MARKETLAB_DB_URI')
if not ENGINE_URI:
    raise RuntimeError('MARKETLAB_DB_URI is not set. Put credentials in /home/msands/.openclaw/workspace/.env')
OUT_CSV = f'/home/msands/.openclaw/workspace/skills/backtest/agentic/{date.today().isoformat()}_backtest_results.csv'

np.seterr(all='ignore')

# ---------- Data ----------
engine = create_engine(ENGINE_URI)
with engine.connect() as c:
    px = pd.read_sql(text('select date,ticker,adj_px from prices order by date'), c)
    macro = pd.read_sql(text('select date, "VIX_LVL" as vix, "CPI_YOY" as cpi_yoy, "FEDFUNDS_LVL" as fed, "GS10_LVL" as gs10, "DTB3_LVL" as dtb3, "M2_YOY" as m2_yoy, "INDPRO_YOY" as indpro_yoy, "UNEMP_LVL" as unemp, "SP500_YOY" as sp500_yoy from macro order by date'), c)
    syc = pd.read_sql(text('select date,yield_type,"10_yr" as y10,"2_yr" as y2,"3_mo" as y3m from sovereign_yield_curve where country=\'US\' order by date'), c)

px['date'] = pd.to_datetime(px['date'])
P = px.pivot(index='date', columns='ticker', values='adj_px').sort_index()
R = P.pct_change(fill_method=None)

# Investable ETF universe with long history in db
U = [x for x in ['SPY.US','IWB.US','IWF.US','IWD.US','IWM.US','IWR.US','IWP.US','IWS.US','IWN.US','IWO.US','EFA.US','EEM.US','MTUM.US','QUAL.US','USMV.US','VLUE.US','SIZE.US'] if x in P.columns]
R = R[U]

# ACWI proxy from available data
acwi = (0.60 * R['SPY.US'].fillna(0) + 0.30 * R['EFA.US'].fillna(0) + 0.10 * R['EEM.US'].fillna(0)).rename('ACWI_PROXY')

macro['date'] = pd.to_datetime(macro['date'])
M = macro.set_index('date').sort_index().reindex(R.index, method='ffill')

syc['date'] = pd.to_datetime(syc['date'])
Y = syc[syc['yield_type'].isin(['benchmark', 'par'])].sort_values('date').drop_duplicates(['date'], keep='first').set_index('date')
Y = Y[['y10', 'y2', 'y3m']].reindex(R.index, method='ffill')
M['slope_10_2'] = Y['y10'] - Y['y2']
M['slope_10_3m'] = Y['y10'] - Y['y3m']

# ---------- Features ----------
feat = pd.DataFrame(index=R.index)
for lb in [5, 21, 63, 126, 252]:
    feat[f'acwi_mom_{lb}'] = (1 + acwi).rolling(lb).apply(np.prod, raw=True) - 1
    feat[f'acwi_vol_{lb}'] = acwi.rolling(lb).std() * np.sqrt(252)

for c in ['vix','cpi_yoy','fed','gs10','dtb3','m2_yoy','indpro_yoy','unemp','sp500_yoy','slope_10_2','slope_10_3m']:
    feat[c] = M[c]

# standardized macro deltas
for c in ['vix','cpi_yoy','fed','gs10','dtb3','m2_yoy','indpro_yoy','unemp']:
    feat[f'{c}_d1'] = feat[c].diff(1)
    feat[f'{c}_d21'] = feat[c].diff(21)

# asset-level features appended per asset later

def perf(port):
    x = port.dropna()
    if len(x) < 756:
        return None
    b = acwi.reindex(x.index).fillna(0)
    nav = (1 + x).cumprod()
    yrs = (x.index[-1] - x.index[0]).days / 365.25
    if yrs <= 0:
        return None
    cagr = nav.iloc[-1] ** (1/yrs) - 1
    vol = x.std() * np.sqrt(252)
    sharpe = (x.mean() * 252) / (vol + 1e-12)
    ex = x - b
    te = ex.std() * np.sqrt(252)
    ir = (ex.mean() * 252) / (te + 1e-12)
    dd = (nav / nav.cummax() - 1).min()
    return {
        'CAGR': float(cagr),
        'Vol': float(vol),
        'Sharpe': float(sharpe),
        'MaxDD': float(dd),
        'AnnExcessRet': float(ex.mean() * 252),
        'TrackingErr': float(te),
        'InfoRatio': float(ir),
        'TotalReturn': float(nav.iloc[-1] - 1),
        'obs_days': int(len(x)),
        'start': str(x.index[0].date()),
        'end': str(x.index[-1].date()),
    }

# ---------- Econometric model search ----------
# Cross-asset rolling ridge regression on next-day excess returns

def ridge_fit(X, y, lam):
    # closed form ridge with intercept in X already
    XtX = X.T @ X
    I = np.eye(X.shape[1])
    I[0, 0] = 0.0  # don't penalize intercept
    beta = np.linalg.pinv(XtX + lam * I) @ (X.T @ y)
    return beta

results = []

train_min = 504  # ~2 years
retrain_freq = 21

mom_lbs = [21, 63, 126, 252]
vol_lbs = [21, 63]
lams = [1.0, 5.0, 10.0, 25.0, 50.0, 100.0]
sel_k = [1, 2, 3]
cash_thresholds = [0.0, 0.00005, 0.0001, 0.0002]
vol_targets = [0.10, 0.12, 0.15]
lev_caps = [1.0, 1.25, 1.5, 2.0]

for mom_lb in mom_lbs:
    for vol_lb in vol_lbs:
        # build per-asset predictors
        pred = {}
        for a in U:
            df = feat.copy()
            df['asset_mom'] = (1 + R[a].fillna(0)).rolling(mom_lb).apply(np.prod, raw=True) - 1
            df['asset_vol'] = R[a].rolling(vol_lb).std() * np.sqrt(252)
            df['asset_ret1'] = R[a]
            df['asset_ret5'] = (1 + R[a].fillna(0)).rolling(5).apply(np.prod, raw=True) - 1
            df['asset_ret21'] = (1 + R[a].fillna(0)).rolling(21).apply(np.prod, raw=True) - 1
            # target: next-day excess over ACWI
            y = (R[a] - acwi).shift(-1)
            pred[a] = (df, y)

        # common index where features are mostly available
        idx = R.index

        for lam in lams:
            # precompute rolling predictions for each asset
            pmat = pd.DataFrame(index=idx, columns=U, dtype=float)

            last_fit = None
            betas = {a: None for a in U}

            for i, dt in enumerate(idx[:-1]):
                if i < train_min:
                    continue

                if (last_fit is None) or ((i - last_fit) >= retrain_freq):
                    # refit each asset-specific model with expanding window
                    for a in U:
                        Xall, yall = pred[a]
                        X = Xall.iloc[:i].copy()
                        y = yall.iloc[:i].copy()
                        d = pd.concat([X, y.rename('y')], axis=1).dropna()
                        if len(d) < train_min:
                            betas[a] = None
                            continue
                        Xa = d.drop(columns=['y']).values
                        ya = d['y'].values
                        Xa = np.column_stack([np.ones(len(Xa)), Xa])
                        betas[a] = ridge_fit(Xa, ya, lam)
                    last_fit = i

                # predict today for tomorrow
                for a in U:
                    b = betas[a]
                    if b is None:
                        continue
                    Xrow = pred[a][0].iloc[i]
                    if Xrow.isna().any():
                        continue
                    xv = np.r_[1.0, Xrow.values]
                    pmat.at[dt, a] = float(xv @ b)

            # strategy from forecasts
            for k in sel_k:
                for cth in cash_thresholds:
                    # equal weight top-k positive forecasts
                    w = pd.DataFrame(0.0, index=idx, columns=U)
                    for dt, row in pmat.iterrows():
                        s = row.dropna().sort_values(ascending=False)
                        if len(s) < k:
                            continue
                        if s.iloc[0] <= cth:
                            continue
                        picks = s.index[:k]
                        w.loc[dt, picks] = 1.0 / k

                    # execute next day
                    base = (w.shift(1).fillna(0.0) * R.fillna(0.0)).sum(axis=1)

                    for tv in vol_targets:
                        for cap in lev_caps:
                            rv = base.rolling(21).std() * np.sqrt(252)
                            lev = (tv / (rv + 1e-12)).clip(lower=0.0, upper=cap)
                            port = (lev.shift(1).fillna(0.0) * base).fillna(0.0)
                            st = perf(port)
                            if st is None:
                                continue
                            name = f'RIDGE_XASSET_m{mom_lb}_v{vol_lb}_lam{lam}_k{k}_ct{cth}_tv{tv}_cap{cap}'
                            desc = 'Rolling expanding-window ridge regressions by asset forecasting next-day excess vs ACWI proxy; top-k long-only selection with cash threshold and vol targeting overlay.'
                            sig = f'Features include macro levels/deltas, yield-curve slopes, ACWI momentum/vol, and asset momentum/vol/short returns. Refit every {retrain_freq} days, train min {train_min} days.'
                            results.append({'Strategy': name, 'Benchmark': 'MSCI ACWI proxy (60% SPY/30% EFA/10% EEM)', 'Description': desc, 'Signal_Calc': sig, **st})

# also add strong baseline family for comparison
for th in [14, 16, 18, 20, 22]:
    sig = (M['vix'] < th).astype(float).shift(1).fillna(0)
    if {'IWF.US','USMV.US'}.issubset(U):
        p = sig * R['IWF.US'].fillna(0) + (1 - sig) * R['USMV.US'].fillna(0)
        st = perf(p)
        if st:
            results.append({'Strategy': f'VIXSW_{th}_IWF_USMV', 'Benchmark': 'MSCI ACWI proxy (60% SPY/30% EFA/10% EEM)', 'Description': 'Volatility regime switch between growth and minimum-volatility.', 'Signal_Calc': f'If VIX<{th} long IWF else USMV with 1-day lag.', **st})

res = pd.DataFrame(results)
if res.empty:
    raise RuntimeError('No strategies produced')

res = res.sort_values(['InfoRatio','Sharpe','AnnExcessRet'], ascending=[False, False, False]).reset_index(drop=True)
res.to_csv(OUT_CSV, index=False)

# find satisfying strategies
hit = res[(res['AnnExcessRet'] >= 0.01) & (res['Sharpe'] > 1.0)]

print('WROTE', OUT_CSV)
print('N_STRATEGIES', len(res))
print('N_HITS', len(hit))
if len(hit):
    print('TOP_HITS')
    print(hit[['Strategy','Sharpe','AnnExcessRet','InfoRatio','CAGR','MaxDD']].head(20).to_string(index=False))
else:
    print('TOP_OVERALL')
    print(res[['Strategy','Sharpe','AnnExcessRet','InfoRatio','CAGR','MaxDD']].head(20).to_string(index=False))