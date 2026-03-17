---
name: market-brief
description: Write a daily market summary report for the asset allocation team fund managers.
---

## Investable Universe
- Within Equities, I invest in: Russell 1000, Russell 1000 Growth, Russell 1000 Value, Russell Mid Cap, Russell Mid Cap Growth, Russell Mid Cap Value, Russell 2000, MSCI EAFE, MSCI EM.
- Within Fixed Income, I invest in: Long Duration US Treasuries (TLT), Short Duration US Treasuries (SHV), US Aggregate Bond Index (AGG), US High Yiled (HYG), and US TIPs (TIP).

## Background
- I am a fund manager on the asset allocation team managing a series of Target Date and Target Risk Funds. 
- My funds are multi-asset class portfolios that invest in both equities and fixed income securities.
- Consider the investments/indices above as representative of my investable universe. Relevnt impact statements and analysis should in some way tie back to actionable decisions on this universe.
- Write the report from a cross sectional perspective. Asset Allocators make zero-sum decisions. Everything must be understand in the context of other available opportunity sets. Structure the report in terms of broad categories, with each country being shown comparatively to the others, within that same category.

## API Access ##
I have stored API keys for Fred and EODHD in a file called .env in the working directory. You may use these APIs as needed, but be conscious of API limits and do not needlessly pull data. If you need it, pull it.

# Order
- The report should be structured with broad sections in the following order: 
- Within each section, subsections should use the following order: US Equities, International Developed Equities, EM Equities, US Fixed Income.


## DAILY BRIEF PROMPT
Generate my Daily Market Intelligence Brief PDF for today. This is a comprehensive pre-market morning report covering:

**HEADLINE SUMMARY**
- Key themes/narrative/headlines that are driving markets and relevant to consider. Provide links.

**EARNINGS & VALUATIONS DASHBOARD** — Include current data for:
- For each index within the investable universe
    - * ALL earnings and valuation data MUST be the most recent data available. You cannot use stale data that is no longer relevant. Data should not be more than two weeks old. Use LSEG and Factset for the appropriate most recent links* https://lipperalpha.refinitiv.com/2026/03/sp-500-earnings-dashboard-25q4-march-6-2026/; https://lipperalpha.refinitiv.com/wp-content/uploads/2026/03/TRPR_82201_20260306.pdf; https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_030626.pdf; https://insight.factset.com/
    - Forward P/E
    - Trailing P/E, 
    - Comparison of Forward P/E to Avg. Forward P/E over the past 20Y (or max data). Show percentile rank.
    - Comparison of Trailing P/E to Avg. Trailing P/E over the past 20Y (or max data). Show percentile rank.
    - Blended Forward EPS Growth Estimate
    - Next 12 months EPS Growth Estimate
    - Comparison of Blended Forward EPS Growth Estimate to Avg. Forward Forward EPS Growth over the past 20Y (or max data). Show percentile rank.
    - Show comparative chart of EPS estimates for each index over the recent past.
    - Show comparative chart of the ratio of relevent indices P/E ratios to a relevant comporable over time (i.e. Ratio of Russell 1000 Growth PE to Russell 1000 Value PE). Annotate the average and standard deviations.

**EARNINGS REVIEW** — Search for and include:
- Q4 (or most recent) earnings season scorecard: % reported, % beating EPS & revenue, blended EPS growth YoY, revenue growth YoY, FY forward estimates
- Sector-level EPS growth breakdown
- Notable recent earnings beats/misses from major companies this week
- Forward guidance commentary and risk flags (tariffs, margins, etc.)

**FIXED INCOME — RATES, SPREADS & DURATION** — Search for current data:
- US Treasury Yields: 2Y, 5Y, 10Y, 30Y with changes vs. 1M ago and 1Y ago
- Yield curve spreads: 2s10s and 5s30s; shape assessment (flat/steep/inverted)
- Investment Grade (IG) corporate OAS: current bp, percentile rank, duration, signal
- High Yield (HY) corporate OAS: current bp, percentile rank, signal; CCC tier separately
- EM sovereign spread context
- TIPS breakeven inflation: 5Y and 10Y; real yield estimates
- Fixed income strategy summary table: each asset, all-in yield, today's signal, rationale
- Duration risk commentary
- Fed Funds and Interest Rate expectations


**MACRO DATA** — For each market-moving economic release today, provide:
- Executive snapshot table: Actual vs. Forecast vs. Prior, Surprise direction
- Full data panel per release (5-column: Actual, Forecast, Prior, Surprise, Trend)
- Key Highlights (bullet points)
- Detailed Commentary & Market Implications
- Metadata
  - Full url to the source report.
  - Date and time the report was released.
  - Date and time you accessed the report.
- Headline print
  - Actual figure(s) reported (e.g. CPI MoM, NFP change, GDP QoQ SAAR). Source from the official report directly.
  - Consensus estimate(s) for the same metric (e.g. consensus NFP change). Explicitly state the source you retrieve this from.
  - Prior figure(s) for the same metric (e.g. prior month CPI MoM). Source from the official report directly.
- Notable sub-components
  - Extract any key sub-components of the report that are particularly relevant or market-moving. For example, if the headline print is CPI MoM, extract core CPI MoM, shelter index change, energy index change, etc. If the headline print is NFP change, extract private payrolls change, manufacturing payrolls change, average hourly earnings change, etc.
  - Provide both quantitiative (specific data) and qualitative assessments.
- Confounding Events
  - Note any major events, policy changes, or external factors that may have influenced the data. For example, if there was a major weather event that disrupted economic activity during the month, note this as a potential confounding factor when interpreting the data. 
  - Anything unusually important that may have influenced the data should be noted here.
- Direct Quotations
  - Extract any direct quotations from the report or press release that are particularly relevant or insightful. For example, if the BLS report includes a statement from the Commissioner about the labor market, extract that quote and include it here. If specific explanations or caveats are mentioned in the report, quote those directly.
- Market Interpretation
  - Provide a brief interpretation of what the data means for the economy and markets. For example, if CPI came in hotter than expected, you might interpret this as increasing the likelihood of more aggressive Fed tightening, which could be negative for equities and positive for bonds. If NFP came in much stronger than expected, you might interpret this as a sign of a resilient labor market, which could have implications for consumer spending and economic growth.
  - Scan external sources for any notable market reactions to the data release (e.g. stock market down 1% following a hot CPI print) and include that in your interpretation with explicit sourcing.
  - Interpret this specific report in the context of the broader macro environment and recent trends. For example, if this is a CPI report, consider how it fits into the recent trend of inflation data and what it might signal about the trajectory of inflation going forward. Consider how it relates to other economic data that has been released recently, such as labor market data, consumer spending data, etc.
- Conclusion
  - Provide a brief conclusion (1-2 sentences) on how this may impact my fund's positioning or strategy.
**7. FORWARD CALENDAR** — This week's upcoming releases with dates, times (ET/GMT), region, impact level, and consensus estimates; plus 3-5 key themes and watch points for the week


**MARKET SENTIMENT** — Search for current readings:
- VIX level and interpretation (fear/greed zone)
- CBOE Equity Put/Call ratio, Total Put/Call ratio, SPX Put/Call ratio
- Option implied volatility analysis and percentile ranks
- Recent fund flow data (US equity vs. international equity inflows/outflows)
- Contrarian signals and conclusions

**MARKET IMPACT BY INDEX** — Comprehensive analysis for each:
- For each index in the investable universe, describe Today's Signal, Key Drivers, Detailed Impact Commentary.
- In table format, 


**Ouput**
Write the comprehensive market brief and respond to user with the report. 