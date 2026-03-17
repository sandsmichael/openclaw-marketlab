# Daily Market Brief — 2026-03-13

## Executive Snapshot
- U.S. equities sold off sharply on Thursday: S&P 500 closed at **6,672.62**, down **1.52% d/d** and **1.00% vs last Friday**. (Postgres; prices)
- Style drawdown was broad, with **growth underperforming value** and **small caps underperforming large caps**: IWF proxy **-1.79%**, IWP proxy **-2.31%**, IWO proxy **-2.54%** versus IWD proxy **-0.87%**, IWS proxy **-1.65%**, IWN proxy **-1.63%**. (Postgres; constituents+prices)
- Defensive/real-asset leadership was clear inside U.S. sectors: **Energy +1.00%**, **Utilities +0.72%**, **Consumer Defensive +0.09%**, while **Industrials -2.53%** and **Consumer Cyclical -2.23%** lagged. (Postgres; constituents+prices)
- Rates/credit backdrop remains restrictive: UST 2Y at **3.64%** and 10Y at **4.21%** (2s10s **+57 bp**), HY OAS at **3.09%**. (Web; FRED DGS2/DGS10/BAMLH0A0HYM2)

## 1) Cross-Asset Highlights (What happened yesterday / this week)
### U.S. Equities
- Mega-cap tech was a primary index drag: AAPL **-1.94%**, NVDA **-1.55%**, META **-2.55%**, TSLA **-3.14%**, AMZN **-1.47%**. (Postgres; prices+constituents)
- Sector dispersion indicates a risk-off rotation with cyclical duration (tech/discretionary/industrials) de-rated while defensives and energy outperformed. (Postgres; constituents+prices)

### Rates & Credit
- UST yields re-priced higher over the past week: 2Y moved from **3.56% (Mar 6)** to **3.64% (Mar 11)** and 10Y from **4.15%** to **4.21%**. (Web; FRED DGS2/DGS10)
- HY spread is still contained at **3.09%** after a modest widening versus late February (**2.86% on Feb 20**). (Web; FRED BAMLH0A0HYM2)

### Commodities / Alternatives
- WTI rose from **$90.77 (Mar 6)** to **$94.65 (Mar 9)**, consistent with energy sector leadership in equities. (Web; FRED DCOILWTICO)
- Crypto risk beta stayed firm: Bitcoin at **$72,812** (**+3.43% 24h**) and Ethereum at **$2,148** (**+3.99% 24h**). (Web; CoinGecko)

## 2) New Economic Data & Macro Events
- This week’s inflation prints were in line on headline/core CPI: Feb CPI **+0.3% m/m**, **+2.4% y/y**; core CPI **+0.2% m/m**, **+2.5% y/y**. (Web; MarketWatch calendar)
- Yesterday’s labor/housing/trade releases were mixed-to-better on activity: jobless claims **213k** (vs **215k** consensus), housing starts **1.49m** (vs **1.35m**), trade deficit **-$54.5bn** (vs **-$67.0bn**). (Web; MarketWatch calendar)
- This morning’s 8:30 ET block was softer on growth but somewhat cooler on inflation: Q4 GDP first revision **0.7%** (vs **1.5%** consensus), PCE y/y **2.8%** (vs **2.9%**), core PCE y/y **3.1%** (in line). (Web; MarketWatch calendar)
- Next week focus: **FOMC decision Wednesday 2:00 PM ET** and Powell press conference at **2:30 PM ET**. (Web; MarketWatch calendar)

## 3) Risk-On / Risk-Off Signal
- Current tape reads **mild risk-off in equities, not full stress**: broad style-box losses, cyclical underperformance, and defensive sector leadership point to de-risking. (Postgres; constituents+prices)
- Credit is not confirming a disorderly risk-off regime: HY OAS at **3.09%** is above recent tights but far from crisis-style widening. (Web; FRED BAMLH0A0HYM2)
- Net: tactical caution remains warranted into FOMC; policy-path uncertainty still outweighs single-data-point relief on inflation. (Web; MarketWatch + FRED)

## 4) Notable Moves Across Covered Asset Classes
- **U.S. style equity (Russell-style proxy baskets):** LGrowth **-1.79%**, LValue **-0.87%**, MGrowth **-2.31%**, MValue **-1.65%**, SGrowth **-2.54%**, SValue **-1.63%**. (Postgres; constituents+prices)
- **International developed / EM:** reliable in-database daily index series were not available in this environment for today’s cut; omitted rather than estimated. (Postgres; table coverage check)
- **Fixed income sleeves (Treasury duration / TIPS / HY):** UST curve is positively sloped at **+57 bp (10Y–2Y)** and HY spread is **3.09%**. (Web; FRED DGS2/DGS10/BAMLH0A0HYM2)
- **Commodities / crypto watchlist:** WTI impulse higher and crypto positive 24h momentum suggest selective risk appetite outside core U.S. equities. (Web; FRED DCOILWTICO + CoinGecko)

## 5) Implications for Target Date / Target Risk Funds
1. **Equity sleeve:** Keep a near-term quality/defensive bias inside U.S. equities; growth duration remains vulnerable if real yields stay firm into/after FOMC. (Postgres; constituents+prices + Web; FRED)
2. **Rates sleeve:** With 2Y/10Y back up and growth data softening, barbell exposure across intermediate Treasuries plus selective credit remains preferable to adding pure beta. (Web; FRED + MarketWatch)
3. **Credit sleeve:** HY spread behavior is watchful but not alarming; maintain carry but avoid lower-quality concentration until post-FOMC direction is clearer. (Web; FRED)
4. **Real assets / inflation hedge:** Energy strength argues to keep modest real-asset diversification alive, but size risk given macro growth deceleration signals. (Postgres; sectors + Web; FRED/MarketWatch)

---
### Method / Data Notes
- U.S. style-box returns above are computed as **constituent-weighted one-day returns** using latest available constituent files and daily adjusted prices in MarketLab. (Postgres; constituents+prices)
- Coverage caveat: some universes had partial daily pricing coverage (e.g., IWO/IWN constituents), but signal direction was consistent across all six style buckets. (Postgres; constituents+prices)
