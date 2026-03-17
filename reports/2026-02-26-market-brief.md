# Daily Market Brief — 2026-02-26

## 1) Cross-Asset Highlights (What happened + what matters next)

- U.S. equities finished higher on 2/25, with the broad market up **+0.84%** (SPY proxy), while leadership stayed tilted to growth over value (**Russell 1000 Growth +1.29%** vs **Russell 1000 Value +0.29%**). (Postgres; prices)
- Small caps lagged on a relative basis: **Russell 2000 +0.47%** on the day and roughly flat week-to-date (**-0.01%**), versus **Russell 1000 +0.43% WTD**. (Postgres; prices)
- International equities participated but remain mixed for the week: **MSCI EAFE +0.96% day / +0.72% WTD** and **MSCI EM +1.10% day / +1.56% WTD**. (Postgres; prices)
- Rates remain in a modestly steep positive-slope regime: U.S. Treasury par yields at last print were **2Y 3.48%**, **10Y 4.08%**, **30Y 4.72%**; 2s10s spread near **+60 bps**. (Postgres; sovereign_yield_curve)
- Near-term macro catalyst path is front-loaded into Friday and next week: **Jan PPI consensus +0.3% m/m (core +0.4%)** on 2/27, then **ISM Manufacturing consensus 52.6** (3/2), **ADP 22k** (3/4), and **Nonfarm Payrolls 130k / unemployment 4.4%** (3/6). (Web; MarketWatch Economic Calendar)

## 2) Macro Data & Policy Context

- This week’s U.S. data has leaned “not recessionary, but not re-accelerating”: **consumer confidence 91.2 vs 88.6 consensus** and **initial jobless claims 215k vs 206k consensus** (soft miss, but still low absolute claims). (Web; MarketWatch Economic Calendar)
- Last week’s inflation prints came in sticky enough to keep policy caution alive: **PCE y/y 2.9%** and **core PCE y/y 3.0%** (Dec release), while Q4 GDP printed **1.4%** versus **2.5%** consensus. (Web; MarketWatch Economic Calendar)
- Market-implied volatility/risk premium proxies remain contained in local context: **VIX 16.34** (latest macro print) and **corporate spread 1.61** (vs **1.62** prior month snapshot). (Postgres; macro)

## 3) Risk-On / Risk-Off Dashboard

**Current read: Mild risk-on, but selective.**

- **Pro risk-on:** Growth leadership persists (**IWF +1.29% day, +1.02% WTD**) and EM is outperforming DM/U.S. week-to-date (**EEM +1.56% WTD**). (Postgres; prices)
- **Neutral/caution:** Value and small-cap breadth are softer (**IWD -0.10% WTD; IWN -0.58% WTD**) and jobless claims were above consensus this morning. (Postgres; prices; Web; MarketWatch Economic Calendar)
- **Rates backdrop:** 2Y up about **+1 bp** over the last ~week while 10Y is down about **-1 bp** (using 2/12 vs 2/20 snapshots), implying no clean reflation signal yet. (Postgres; sovereign_yield_curve)

## 4) Notable Asset-Class Moves (Aligned to strategic coverage)

### U.S. Equity Style (Russell Proxy ETFs)
- Large Growth: **+1.29% day / +1.02% WTD** (IWF). (Postgres; prices)
- Large Value: **+0.29% day / -0.10% WTD** (IWD). (Postgres; prices)
- Mid Growth: **+0.70% day / +0.05% WTD** (IWP). (Postgres; prices)
- Mid Value: **+0.09% day / -0.22% WTD** (IWS). (Postgres; prices)
- Small Growth: **+0.41% day / +0.53% WTD** (IWO). (Postgres; prices)
- Small Value: **+0.45% day / -0.58% WTD** (IWN). (Postgres; prices)

### Non-U.S. Equity
- International Developed (MSCI EAFE proxy): **+0.96% day / +0.72% WTD**. (Postgres; prices)
- Emerging Markets (MSCI EM proxy): **+1.10% day / +1.56% WTD**. (Postgres; prices)

### Fixed Income / Credit (Policy-sensitive snapshot)
- U.S. curve remains upward-sloping at last available close (**2Y 3.48%, 10Y 4.08%, 30Y 4.72%**). (Postgres; sovereign_yield_curve)
- Credit stress still low by recent standards with **corp spread 1.61** and **VIX 16.34**. (Postgres; macro)
- Note: direct daily ETF pricing for TIPS/high-yield sleeves was not available in the Postgres feed used for this brief. (Postgres; prices)

### Real/Alternative Signals (monitor list)
- Gold proxy closed near **$18.63** on 2/25, up **+0.49%** on the day and **+2.64% WTD**, suggesting ongoing hedge demand despite equities being firm. (Postgres; prices)
- No reliable in-feed daily prints were available for silver/copper/broad commodities/crypto proxies in this run; omitted to avoid low-confidence figures. (Postgres; prices)

## 5) Implications for Target Date / Target Risk Funds

1. **Keep equity beta, but favor quality growth over broad high-beta cyclicality.**
   - Growth leadership plus contained volatility supports staying invested, but weak value/small-cap relative breadth argues against aggressively adding cyclical beta into payroll week. (Postgres; prices; Postgres; macro)

2. **In fixed income, preserve duration balance and avoid over-chasing credit spread compression.**
   - With 2s10s positive and macro still mixed, barbell-like duration exposure remains reasonable; credit remains constructive but already tight enough to limit incremental reward. (Postgres; sovereign_yield_curve; Postgres; macro)

3. **Use next-week data (ISM + payrolls) as a tactical risk checkpoint.**
   - A downside labor surprise versus **130k payroll consensus** and **4.4% unemployment consensus** would likely favor adding quality duration and trimming lower-quality equity beta; upside surprise supports maintaining current pro-risk tilt. (Web; MarketWatch Economic Calendar)

---

## Bottom Line

Markets are behaving **risk-on at the index level but narrow under the surface**: growth and EM are carrying, while value/small-cap participation is softer. Into Friday PPI and next week’s payroll cluster, portfolios should remain invested but selective—favoring resilient equity exposures and balanced duration rather than broad cyclical/chasing trades. (Postgres; prices; Postgres; macro; Web; MarketWatch Economic Calendar)
