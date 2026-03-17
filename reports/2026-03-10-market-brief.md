# Daily Market Brief — 2026-03-10

## Executive Take
US risk tone improved into Monday’s close, led by growth and smaller-cap growth cohorts, while value and defensives lagged less but still finished positive. The immediate macro focus is inflation and labor-sensitive releases (CPI Wednesday; claims/housing Thursday; GDP revision + PCE/income/spending Friday), which likely sets the next rates-and-duration impulse for multi-asset portfolios. (Postgres; prices/constituents, Web; MarketWatch calendar)

## 1) Cross-Asset Highlights (What happened / What matters this week)
- **US equities rebounded:** S&P 500 proxy return was **+0.84%** on 2026-03-09 vs 2026-03-06, while broad US (Russell 3000 proxy via IWB universe) was **+0.85%**. (Postgres; prices/constituents)
- **Style leadership favored growth:** Large Growth proxy (IWF universe) **+1.21%** vs Large Value (IWD universe) **+0.46%**; Mid Growth (IWP) **+1.20%** vs Mid Value (IWS) **+0.59%**; Small Growth (IWO) **+1.77%** vs Small Value (IWN) **+0.53%**. (Postgres; prices/constituents)
- **Small caps participated:** Russell 2000 proxy (IWM universe) rose **+1.17%** day/day, confirming broader risk participation beyond mega-cap tech. (Postgres; prices/constituents)
- **Rates/credit backdrop (latest available):** US Treasury curve snapshot shows **2Y 3.48%**, **10Y 4.08%**, **30Y 4.72%** (dated 2026-02-20); macro credit spread series sits at **1.61%** (latest monthly point 2026-02-28). (Postgres; sovereign_yield_curve, macro)
- **This week’s event risk:** CPI (Wed), claims + housing starts/permits (Thu), and GDP revision + PCE + spending + durable goods + JOLTS + Michigan sentiment (Fri) are clustered and could reset near-term policy/risk expectations. (Web; MarketWatch calendar)

## 2) New Economic Data / Macro Events
- **Last week labor surprise:** February payrolls printed **-92k** vs **+50k** consensus; unemployment rate was **4.4%** vs **4.3%** consensus; average hourly earnings **+0.4% m/m** vs **+0.3%** consensus. (Web; MarketWatch calendar)
- **NFIB today (already released):** **98.8** vs **99.5** consensus, a mild downside miss. (Web; MarketWatch calendar)
- **Key setup into tomorrow CPI:** Market is looking for **+0.3% m/m headline CPI**, **2.4% y/y headline**, **+0.2% m/m core**, **2.5% y/y core**. (Web; MarketWatch calendar)

## 3) Risk-On / Risk-Off Read
- **Risk-on evidence:** Growth outperformed value across large/mid/small cohorts, and tech/communication services were the top two S&P sector contributors by weighted return (**Tech +1.70%**, **Comm Services +1.22%**). (Postgres; prices/constituents)
- **Not a full “all-clear”:** Financials (**-0.50%**) and Energy (**-0.43%**) lagged; market breadth was close to balanced (**1,277 advancers / 1,256 decliners / 22 unchanged**), implying selective rather than indiscriminate risk-taking. (Postgres; prices/constituents)
- **Volatility tone improved at month-end:** VIX monthly series eased from **17.44** (2026-01-31) to **16.34** (2026-02-28), consistent with calmer but not complacent conditions. (Postgres; macro)

## 4) Notable Moves Across Asset Classes
- **US sector leadership:** Tech led at **+1.70%**, then Communication Services **+1.22%**, Healthcare **+0.98%**; laggards were Financial Services **-0.50%** and Energy **-0.43%**. (Postgres; prices/constituents)
- **Single-name breadth in S&P basket:** Top movers included **SNDK +11.64%**, **TER +8.57%**, **CIEN +8.28%**; weakest included **AJG -4.54%**, **CF -4.09%**, **CHTR -4.06%**. (Postgres; prices/constituents)
- **International equity/fixed-income/commodities/crypto:** Reliable same-day benchmark prints for MSCI EAFE/EM and non-US risk assets were not consistently available from in-database sources at the daily frequency for this run, so they are omitted rather than inferred. (Postgres coverage check)

## 5) Implications for Target Date / Target Risk Funds
- **Equity sleeve:** Growth beta re-accelerated; avoid chasing one-day style swings ahead of CPI. Tactical tilt remains to quality growth, but keep valuation discipline and rebalance triggers active after sharp factor reversals. (Postgres; prices/constituents, Web; MarketWatch calendar)
- **Fixed income sleeve:** With CPI/PCE concentration this week, maintain balanced duration exposure; use policy-sensitive front-end vs carry-oriented intermediate allocations to avoid overcommitting before inflation prints. (Postgres; sovereign_yield_curve, macro; Web; MarketWatch calendar)
- **Multi-asset risk budgeting:** Near-balanced breadth with narrow sector leadership argues for diversified risk deployment rather than concentrated cyclical bets; keep dry powder for post-data repricing windows. (Postgres; prices/constituents)
- **Private markets context:** Public growth rebound may support private equity mark sentiment at the margin, but policy/data volatility this week is likely more relevant for private credit spread assumptions than one-day equity beta. (Postgres; macro/credit)

---
**Data timestamp notes**
- Daily market move calculations use **2026-03-09 vs 2026-03-06** closes where available. (Postgres; prices)
- Sovereign curve data is the **latest available snapshot (2026-02-20 for US)**; non-US sovereign snapshots are older in this dataset. (Postgres; sovereign_yield_curve)
