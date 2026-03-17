# Daily Market Brief — 2026-03-04

## Executive take
U.S. and non-U.S. risk assets sold off into Tuesday’s close, with the heaviest pressure in emerging markets and international developed equities, while U.S. large-cap growth was comparatively resilient. The near-term macro/risk backdrop is mixed: equity price action is risk-off, but volatility and credit stress gauges remain contained. Next key catalysts are Friday’s U.S. employment report and next Wednesday’s CPI print.

## 1) Cross-asset highlights (what happened yesterday)
- **Broad U.S. equities:** SPY fell **0.88%** on 2026-03-03; 1-week return is **-1.02%**. (Postgres; prices)
- **U.S. style split (Russell proxies):**
  - Large Growth (IWF) **-0.62%** vs Large Value (IWD) **-1.28%** (growth outperformed value by **66 bps**). (Postgres; prices)
  - Mid Growth (IWP) **-0.94%** vs Mid Value (IWS) **-1.61%** (growth outperformed by **67 bps**). (Postgres; prices)
  - Small Growth (IWO) **-2.08%** vs Small Value (IWN) **-1.45%** (value outperformed by **63 bps**). (Postgres; prices)
- **Non-U.S. equities:** MSCI EAFE proxy (EFA) **-3.11%** and MSCI EM proxy (EEM) **-5.01%** on the day; 1-week returns are **-4.37%** and **-6.71%**, respectively. (Postgres; prices)
- **Rates/curve context:** U.S. Treasury par yields (latest available 2026-02-20) were **3.48% (2Y)**, **4.08% (10Y)**, and **4.72% (30Y)**. (Postgres; sovereign_yield_curve)

## 2) Macro releases and near-term event path
- Latest stored U.S. inflation/labor snapshot shows **CPI YoY 2.65%**, **core CPI YoY 2.65%**, **unemployment 4.4%**, and **NFP +50k** (latest non-NaN observations dated 2025-12-31 in this dataset). (Postgres; macro)
- **Next U.S. Employment Situation release:** **Fri, Mar 6, 2026, 8:30 AM ET** (for Feb reference month). (Web; BLS Employment Situation calendar)
- **Next U.S. CPI release:** **Wed, Mar 11, 2026, 8:30 AM ET** (for Feb reference month). (Web; BLS CPI calendar)

## 3) Risk-on / risk-off signals
- **Risk-off in price action:** Daily losses across U.S. style boxes and sharper drawdowns in EAFE/EM indicate de-risking, especially outside U.S. large caps. (Postgres; prices)
- **But stress gauges are not flashing disorderly risk:** VIX is **16.34** (vs **17.44** prior month-end) and corporate spread is **1.61%** (vs **1.62%** prior month-end). (Postgres; macro)
- **Cash hurdle remains high:** 3M T-bill level is **3.60%**, still competitive versus risk assets in a drawdown tape. (Postgres; macro)

## 4) Notable moves by allocation-relevant buckets
- **U.S. equities:** Down across large/mid/small; relative leadership stayed with large growth and (within small caps) value. (Postgres; prices)
- **International developed and EM:** Meaningfully weaker than U.S. benchmarks in both 1-day and 1-week windows. (Postgres; prices)
- **Duration backdrop:** Positive 2s10s slope of roughly **60 bps** (4.08% - 3.48%) suggests a normalized curve versus prior inversion periods, but still with elevated long-end yields. (Postgres; sovereign_yield_curve)
- **Commodities/crypto and private markets:** No reliable in-database daily series available in this environment for today’s cut; omitted rather than estimated. (Postgres; prices universe review)

## 5) Implications for target date / target risk portfolios
- **Near-term portfolio stance:** Favor balance over aggressive beta adds until payroll/CPI pass; current tape rewards quality and liquidity. (Postgres; prices; Web; BLS calendars)
- **Equity implementation:** If rebalancing into weakness, phase entries and bias toward higher-quality U.S. large cap sleeves; monitor whether EAFE/EM weakness stabilizes before adding international risk. (Postgres; prices)
- **Fixed income role:** With front-end cash yields still elevated and curve positive, barbell positioning (liquidity + selective duration) remains a practical way to carry defensiveness while preserving optionality. (Postgres; macro; sovereign_yield_curve)
- **Risk controls:** Keep drawdown guardrails tight in higher-vol sleeves (small growth / EM), and reassess after Friday labor and next week CPI. (Postgres; prices; Web; BLS calendars)

---
*Prepared for Asset Allocation Team pre-open review.*