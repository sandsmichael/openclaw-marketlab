---
name: econ-release
description: Fetch and summarize official economic release reports, providing insights and market interpretations.
---

When invoked, fetch the official reports for a named economic release reports listed below. Produce a summary report outlined below.


**Summary Contents**
1. Metadata
  - Full url to the source report.
  - Date and time the report was released.
  - Date and time you accessed the report.
2. Headline print
  - Actual figure(s) reported (e.g. CPI MoM, NFP change, GDP QoQ SAAR). Source from the official report directly.
  - Consensus estimate(s) for the same metric (e.g. consensus NFP change). Explicitly state the source you retrieve this from.
  - Prior figure(s) for the same metric (e.g. prior month CPI MoM). Source from the official report directly.
3. Notable sub-components
  - Extract any key sub-components of the report that are particularly relevant or market-moving. For example, if the headline print is CPI MoM, extract core CPI MoM, shelter index change, energy index change, etc. If the headline print is NFP change, extract private payrolls change, manufacturing payrolls change, average hourly earnings change, etc. Use your judgement but include anything that is particularly relevant or insightful.
  - Provide both quantitiative (specific data) and qualitative assessments.
4. Confounding Events
  - Note any major events, policy changes, or external factors that may have influenced the data. For example, if there was a major weather event that disrupted economic activity during the month, note this as a potential confounding factor when interpreting the data. 
  - Anything unusually important that may have influenced the data should be noted here.
5. Direct Quotations
  - Extract any direct quotations from the report or press release that are particularly relevant or insightful. For example, if the BLS report includes a statement from the Commissioner about the labor market, extract that quote and include it here. If specific explanations or caveats are mentioned in the report, quote those directly.
  - Include explanations and color commentary in addition to the raw, quantitative data point.
6. Market Interpretation
  - Provide a brief interpretation of what the data means for the economy and markets. For example, if CPI came in hotter than expected, you might interpret this as increasing the likelihood of more aggressive Fed tightening, which could be negative for equities and positive for bonds. If NFP came in much stronger than expected, you might interpret this as a sign of a resilient labor market, which could have implications for consumer spending and economic growth.
  - Scan external sources for any notable market reactions to the data release (e.g. stock market down 1% following a hot CPI print) and include that in your interpretation with explicit sourcing.
  - Interpret this specific report in the context of the broader macro environment and recent trends. For example, if this is a CPI report, consider how it fits into the recent trend of inflation data and what it might signal about the trajectory of inflation going forward. Consider how it relates to other economic data that has been released recently, such as labor market data, consumer spending data, etc.
7. Conclusion
  - Provide a brief conclusion (1-2 sentences) on how this may impact my fund's positioning or strategy.

**Output**
- Compile this report as well formated, professional, markdown text and return it through the CLI.
- Send your formatted markdown text to me in Slack by posting in openclaw-simon chanell.
- Cite the source agency and URL in parentheses after each data point. E.g. "(BLS; cpi.htm)" or "(BEA; personal-income)"

**Data Sources**
- Always fetch directly from the official government or agency URL listed below. These pages go live the moment the embargo lifts.
- BLS PDF links (e.g. `bls.gov/news.release/cpi.pdf`) are permanent and always serve the most recently published report — prefer these for raw data extraction.
- For BEA releases, the data portal page will show the latest press release and tables.
- Use FRED (`fred.stlouisfed.org`) only as a fallback if the primary page is unavailable.
- Never guess or interpolate numbers. If the page has not yet updated, say so.


---

## Release Directory

### Bureau of Labor Statistics (BLS) — 8:30 AM ET

**Consumer Price Index (CPI)**
- HTML: https://www.bls.gov/news.release/cpi.htm
- PDF:  https://www.bls.gov/news.release/cpi.pdf
- Key: Headline CPI MoM/YoY, Core CPI MoM/YoY, shelter, energy, food

**Producer Price Index (PPI)**
- HTML: https://www.bls.gov/news.release/ppi.htm
- PDF:  https://www.bls.gov/news.release/ppi.pdf
- Key: Headline PPI MoM/YoY, Core PPI MoM/YoY, goods vs. services

**Employment Situation (Nonfarm Payrolls / NFP)**
- HTML: https://www.bls.gov/news.release/empsit.htm
- PDF:  https://www.bls.gov/news.release/empsit.pdf
- Key: NFP, private payrolls, unemployment rate (U-3), participation rate, avg hourly earnings MoM/YoY, prior month revisions

**JOLTS (Job Openings & Labor Turnover)**
- HTML: https://www.bls.gov/news.release/jolts.htm
- PDF:  https://www.bls.gov/news.release/jolts.pdf
- Release time: 10:00 AM ET
- Key: Job openings, hires, quits rate, layoffs

**Initial & Continuing Jobless Claims**
- PDF (DOL weekly release): https://www.dol.gov/ui/data.pdf
- HTML (ETA): https://oui.doleta.gov/unemploy/claims.asp
- Release time: 8:30 AM ET, Thursdays (weekly)
- Key: Initial claims SA, 4-week moving average, continuing claims

**Import & Export Price Index**
- HTML: https://www.bls.gov/news.release/ximpim.htm
- PDF:  https://www.bls.gov/news.release/ximpim.pdf
- Key: Import prices MoM/YoY ex-fuel, export prices MoM/YoY

---

### Bureau of Economic Analysis (BEA) — 8:30 AM ET

**GDP (Advance / Second / Third Estimate)**
- Data portal: https://www.bea.gov/data/gdp/gross-domestic-product
- Press releases: https://www.bea.gov/news/current-releases
- Key: Real GDP QoQ SAAR, PCE contribution, gross private investment, gov't spending, net exports

**Personal Income & Outlays (PCE / Consumer Spending)**
- Data portal: https://www.bea.gov/data/income-saving/personal-income
- Press releases: https://www.bea.gov/news/current-releases
- Key: Personal income MoM, personal spending MoM, PCE deflator MoM/YoY, Core PCE MoM/YoY (Fed's preferred inflation gauge)

---

### U.S. Census Bureau — 8:30 AM ET

**Retail Sales (Advance Monthly)**
- https://www.census.gov/retail/sales.html
- Key: Headline retail sales MoM, ex-auto MoM, control group (ex-auto/gas/food/building), prior revision

**Durable Goods Orders (Advance)**
- https://www.census.gov/manufacturing/m3/adv/current/index.html
- Key: New orders MoM, ex-transportation MoM, core capital goods orders (nondefense ex-aircraft) MoM — leading capex indicator

**Housing Starts & Building Permits**
- https://www.census.gov/construction/nrc/current/index.html
- Key: Total starts SAAR, single-family vs. multifamily, permits SAAR

**New Home Sales**
- https://www.census.gov/construction/nrs/current/index.html
- Release time: 10:00 AM ET
- Key: New home sales SAAR, median price, months of supply

---

### Institute for Supply Management (ISM) — 10:00 AM ET

**ISM Manufacturing PMI** (released 1st business day of month)
- https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/
- Key: Composite PMI, new orders, production, employment, supplier deliveries, prices paid (expansion > 50)

**ISM Services PMI** (released 3rd business day of month)
- https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/services/
- Key: Composite NMI, business activity, new orders, employment, prices paid

---

### Federal Reserve

**FOMC Statement & Press Conference**
- https://www.federalreserve.gov/monetarypolicy/fomc.htm
- Release time: 2:00 PM ET (statement); press conference ~2:30 PM ET
- Key: Rate decision, statement language changes, dot plot (quarterly SEP meetings), forward guidance tone

**Industrial Production & Capacity Utilization**
- https://www.federalreserve.gov/releases/g17/current/
- Release time: 9:15 AM ET
- Key: IP MoM, manufacturing output MoM, capacity utilization rate

**Consumer Credit (G.19)**
- https://www.federalreserve.gov/releases/g19/current/
- Release time: 3:00 PM ET
- Key: Total consumer credit change, revolving (credit cards) vs. nonrevolving

---

### Private & Survey Sources

**Consumer Confidence (Conference Board)**
- https://www.conference-board.org/topics/consumer-confidence`
- Release time: 10:00 AM ET, last Tuesday of month
- Key: Confidence index, present situation, expectations component, jobs plentiful/hard-to-get spread

**University of Michigan Consumer Sentiment**
- https://www.sca.isr.umich.edu/
- Release time: 10:00 AM ET (preliminary: 2nd Friday; final: last Friday of month)
- Key: Overall sentiment, current conditions, expectations, 1-year and 5-year inflation expectations

**Existing Home Sales (NAR)**
- https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales
- Release time: 10:00 AM ET
- Key: Sales SAAR, median price YoY, months of supply, % cash buyers

**ADP National Employment Report**
- https://adpemploymentreport.com/
- Release time: 8:15 AM ET, Wednesday before NFP week
- Key: Private payrolls change, sector breakdown, pay growth — treat as NFP directional signal, not a precise forecast


---

