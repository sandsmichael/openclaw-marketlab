# 2026-02-23 Russell Style + MSCI EM/EAFE Backtest Notes

## Universe
- Russell style ETFs: IWB.US, IWF.US, IWD.US, IWR.US, IWP.US, IWS.US, IWN.US, IWO.US
- Global sleeves: EEM.US (MSCI EM proxy), EFA.US (MSCI EAFE proxy)

## Benchmarks used
- US-only strategies benchmarked to SP500 (SPY.US total return proxy).
- Global EEM/EFA strategies benchmarked to ACWI proxy = 60% SPY + 30% EFA + 10% EEM.

## Strategy families tested
1. Buy & Hold for each sleeve/index ETF.
2. Russell cross-sectional momentum rotations (lookbacks 21/63/126/252, top-k 1/2/3, with and without dual-momentum cash filter).
3. EEM vs EFA relative-strength switches (lookbacks 21/63/126/252, with/without cash filter).
4. Macro regime switches (VIX-threshold and 10Y-2Y slope threshold) between Russell growth and value baskets.
5. Trend following for each ETF (MA cross: 20/100, 20/200, 50/200, 100/200).
6. Russell cross-sectional mean-reversion rotations (lookbacks 5/10/21, top-k 1/2/3).

## Output
- Full ranked metrics table: /home/msands/.openclaw/workspace/skills/backtest/agentic/2026-02-23_backtest_results.csv
- 99 strategy variants included.
