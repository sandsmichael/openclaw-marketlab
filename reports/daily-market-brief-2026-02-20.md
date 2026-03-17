# Daily Market Brief

## 1) Cross-Asset Highlights
- U.S. equities closed weaker at the index level, with SPY at 684.48 and down 0.26% on the day and 1.08% over the last five trading sessions. (Postgres; prices)
- International equities were also soft: MSCI EAFE proxy (EFA) fell 0.28% and MSCI EM proxy (EEM) fell 0.25% on the day. (Postgres; prices)
- Rates were marginally lower across the curve: 5Y UST at 3.65% (-1 bp), 10Y UST at 4.08% (-1 bp), and 30Y UST at 4.70% (-1 bp). (Web; FRED DGS5/DGS10/DGS30)
- Credit tone was mixed: HY OAS rose to 2.88% (+2 bps), while the level remains 4 bps tighter versus five sessions ago. (Web; FRED BAMLH0A0HYM2)
- Volatility firmed: VIX closed at 20.23, up 0.61 points day/day. (Web; FRED VIXCLS)

## 2) Macro / Event Flow
- Today’s U.S. macro prints were softer on growth and firmer on inflation: Q4 GDP came in at 1.4% vs 2.5% consensus; headline PCE was 0.4% m/m and 2.9% y/y; core PCE was 0.4% m/m and 3.0% y/y. (Web; MarketWatch Calendar)
- February flash PMIs showed services at 52.3 and manufacturing at 51.2, with manufacturing down from 52.4 prior. (Web; MarketWatch Calendar)
- Next week’s U.S. calendar is lighter on hard data but includes factory orders (Mon), consumer confidence (Tue), jobless claims (Thu), and delayed January PPI (Fri). (Web; MarketWatch Calendar)

## 3) Risk-On / Risk-Off Signals
- Style leadership tilted defensive inside U.S. equities: Russell 1000 Value proxy (IWD) outperformed Russell 1000 Growth proxy (IWF) by 0.17 percentage points on the day. (Postgres; prices)
- Small caps outperformed large caps: Russell 2000 proxy (IWM) rose 0.23% while Russell 1000 proxy (IWB) fell 0.20%, a spread of +0.44 percentage points. (Postgres; prices)
- Cross-asset risk barometers were cautious: VIX moved up to 20.23 and HY OAS widened 2 bps day/day. (Web; FRED VIXCLS/BAMLH0A0HYM2)
- Inflation compensation was stable rather than easing: 10Y breakeven held at 2.29% and 10Y real yield was 1.79%. (Web; FRED T10YIE/DFII10)

## 4) Notable Moves by Asset Class
### US Equity (Russell Style)
- Large Cap: IWB -0.20%; Growth: IWF -0.32%; Value: IWD -0.15%. (Postgres; prices)
- Mid Cap: IWR -0.09%; Mid Growth: IWP -0.04%; Mid Value: IWS -0.20%. (Postgres; prices)
- Small Cap: IWM +0.23%; Small Growth: IWO +0.23%; Small Value: IWN +0.26%. (Postgres; prices)

### Non-US Equity (MSCI EAFE, MSCI EM)
- MSCI EAFE proxy (EFA): -0.28% day/day, -0.85% over five sessions. (Postgres; prices)
- MSCI EM proxy (EEM): -0.25% day/day, -0.84% over five sessions. (Postgres; prices)

### Fixed Income (UST by duration, TIPS, HY)
- UST curve: 2Y 3.47% (flat), 5Y 3.65% (-1 bp), 10Y 4.08% (-1 bp), 30Y 4.70% (-1 bp). (Web; FRED DGS2/DGS5/DGS10/DGS30)
- TIPS proxy via real yields: 10Y real yield at 1.79% (-1 bp), with 10Y breakeven at 2.29% (flat). (Web; FRED DFII10/T10YIE)
- High yield: ICE BofA HY OAS at 2.88% (+2 bps day/day). (Web; FRED BAMLH0A0HYM2)

### Alternatives / Satellites
- Reliable daily pricing for private equity, private credit, and private real estate benchmarks was not available in current primary sources; omitted per policy. 
- No reliable in-environment daily close feed was available for gold, silver, copper, Bitcoin, or Ethereum under the current source policy; omitted per policy.

## 5) Implications for Target Date / Target Risk Funds
- The combination of softer growth surprise (GDP) and sticky core inflation (core PCE at 3.0% y/y) argues for keeping duration exposure balanced rather than extending aggressively at current long-end yields. (Web; MarketWatch Calendar)
- Equity internals are mixed (small-cap outperformance, but higher VIX and wider HY spreads), which supports neutral risk positioning and preference for quality/value balance over pure beta. (Postgres; prices; Web; FRED VIXCLS/BAMLH0A0HYM2)
- Non-U.S. equity underperformance over both one day and five sessions suggests maintaining disciplined rebalance bands rather than chasing relative weakness into month-end. (Postgres; prices)

## Sources
- Postgres (`marketlab.public.prices`), latest market date observed: 2026-02-19.
- FRED series: DGS2, DGS5, DGS10, DGS30, DFII10, T10YIE, BAMLH0A0HYM2, VIXCLS.
- MarketWatch U.S. Economic Calendar: https://www.marketwatch.com/economy-politics/calendar