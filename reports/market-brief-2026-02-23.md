# Daily Market Brief — 2026-02-23

## Executive Snapshot
- U.S. equities finished last week with a mild risk-on tone: S&P 500 rose **0.69%** Friday and **1.12%** over the week, while small caps (Russell 2000) gained **1.95%** on the week. (Postgres; prices)
- Style leadership remains value/cyclically biased YTD: Russell 1000 Value is **+7.10% YTD** versus Russell 1000 Growth at **-4.11% YTD**; small-cap value is **+10.88% YTD** versus small-cap growth at **+4.35% YTD**. (Postgres; prices)
- International equities continue to lead broad U.S. benchmarks YTD: EAFE proxy **+9.24%**, EM proxy **+13.95%**. (Postgres; prices)
- Treasury curve is still positively sloped but modestly flatter vs last week, with 2y/10y at **+60 bps** (vs **+62 bps** a week ago). (Postgres; sovereign_yield_curve)

## Cross-Asset Market Highlights (What happened)
### Equities (close: 2026-02-20)
| Segment | 1D | 1W | MTD | YTD |
|---|---:|---:|---:|---:|
| S&P 500 | +0.69% | +1.12% | -0.43% | +0.94% |
| Russell 1000 Growth | +0.69% | +1.09% | -2.59% | -4.11% |
| Russell 1000 Value | +0.58% | +1.38% | +2.46% | +7.10% |
| Russell Midcap Growth | +0.21% | +2.44% | +0.37% | -0.58% |
| Russell Midcap Value | +0.67% | +2.15% | +4.56% | +8.94% |
| Russell 2000 Growth | -0.34% | +1.80% | +0.22% | +4.35% |
| Russell 2000 Value | +0.33% | +1.90% | +3.63% | +10.88% |
| MSCI EAFE (ETF proxy) | +0.82% | +0.72% | +4.13% | +9.24% |
| MSCI EM (ETF proxy) | +2.13% | +2.43% | +5.48% | +13.95% |

Source for all rows: (Postgres; prices)

### Rates / Fixed Income
- U.S. Treasury yields (2y/10y/30y) closed at **3.48% / 4.08% / 4.72%**. (Postgres; sovereign_yield_curve)
- Day-over-day move was **+1 bp / 0 bp / +2 bps** and week-over-week move was **+1 bp / -1 bp / 0 bps**. (Postgres; sovereign_yield_curve)
- 2s10s slope sits at **+60 bps**, down from **+62 bps** a week ago (mild flattening). (Postgres; sovereign_yield_curve)

## Macro Releases & Policy Context
- Last Friday’s U.S. releases (per MarketWatch calendar) showed Q4 GDP at **1.4%**, PCE inflation at **2.9% y/y**, core PCE at **3.0% y/y**, and Feb flash PMIs at **51.2** (manufacturing) / **52.3** (services). (Web; MarketWatch Economic Calendar)
- This week’s key U.S. scheduled events include consumer confidence (Tue), initial jobless claims (Thu), and PPI (Fri), with multiple Fed speakers across the week. (Web; MarketWatch Economic Calendar)
- In the internal macro time series, latest monthly Fed funds level is **3.64%** (Jan), while the latest reported VIX level is **16.34** (Feb monthly point), consistent with contained risk pricing. (Postgres; macro)

## Risk-On / Risk-Off Signals
- **Risk-on signal:** Value and smaller-cap sleeves outperformed growth on a 1W and YTD basis in most buckets, pointing to broader cyclical participation rather than narrow mega-cap leadership. (Postgres; prices)
- **Risk-on signal:** EM and EAFE YTD leadership versus S&P 500 suggests improving global beta appetite. (Postgres; prices)
- **Risk-off counter-signal:** Curve flattening at the margin (2s10s down **2 bps** vs prior week) and still-soft growth style MTD (**-2.59%** for Russell 1000 Growth) argue for keeping some defensive ballast. (Postgres; sovereign_yield_curve; prices)

## Asset Allocation Implications (Target Date / Target Risk)
1. **Keep a value/cyclical tilt inside U.S. equities** while retaining strategic growth exposure; current dispersion remains large (**~11.2 pp YTD** gap between Russell 1000 Value and Growth). (Postgres; prices)
2. **Maintain diversified non-U.S. allocation**; international developed and EM remain additive to equity return breadth YTD. (Postgres; prices)
3. **In fixed income, preserve duration balance rather than reach**: a positive curve (**+60 bps 2s10s**) still rewards carry, but flatter week-over-week profile supports a barbelled core (intermediate + long duration hedges) instead of a one-way long-duration bet. (Postgres; sovereign_yield_curve)
4. **Private markets lens:** public small/value resilience and stable volatility backdrop (VIX monthly point **16.34**) are supportive for private equity pacing, while still arguing for disciplined underwriting in private credit as policy/inflation uncertainty persists. (Postgres; prices; macro)

## Data Gaps / Notes
- Reliable, same-timestamp pricing for TIPS ETFs, high-yield ETFs, REITs, commodities, and crypto was not available in Postgres for this run; omitted rather than estimated. (Postgres; prices)
- U.S. economic calendar data sourced from MarketWatch due to missing web search key in this environment. (Web; MarketWatch Economic Calendar)
