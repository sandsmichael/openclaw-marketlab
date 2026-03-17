# Daily Market Brief — 2026-03-16

## Executive snapshot
- **Tone:** Broad **risk-off** into this week’s open: all tracked US style and international equity proxies closed lower Friday, with weakness most visible in non-US and small-cap growth/value exposures. (Postgres; prices)
- **Leadership/laggards:** US large value held up best (+0.03% 1D), while international developed equities lagged (-1.19% 1D). (Postgres; prices)
- **Rates/credit/vol:** Latest available macro market gauges are not signaling stress: VIX at 16.34 and corporate spread at 1.61, both near recent lows in this dataset. (Postgres; macro)

## Cross-asset and style highlights (close: 2026-03-13)
### US equities (Russell style proxies)
- **Broad US beta:** IWB -0.54% (1D), -1.61% (1W), -4.40% (1M). (Postgres; prices)
- **Large-cap style:** IWF -1.13% (1D) vs IWD +0.03% (1D); over 1M both are down similarly (IWF -4.29%, IWD -4.49%). (Postgres; prices)
- **Mid-cap style:** IWP -0.19% (1D) vs IWS -0.08% (1D); 1W drawdown is steeper in growth (-3.00%) than value (-1.97%). (Postgres; prices)
- **Small-cap style:** IWO -0.40% (1D) and IWN -0.29% (1D); both are ~-7% over 1M, showing weaker risk tolerance lower in cap structure. (Postgres; prices)

### Non-US equities
- **Developed ex-US (EFA):** -1.19% (1D), -2.01% (1W), -8.23% (1M). (Postgres; prices)
- **Emerging markets (EEM):** -0.26% (1D), -0.91% (1W), -7.73% (1M). (Postgres; prices)

### Rates and credit
- **US Treasury curve (latest in DB):** 2Y 3.47%, 10Y 4.08%, 30Y 4.70%; 2s10s slope is +61 bps. (Postgres; sovereign_yield_curve)
- **Day-over-day move (latest observation):** 10Y and 30Y each eased ~1 bp vs prior day; 2Y was unchanged. (Postgres; sovereign_yield_curve)
- **Credit and volatility context (latest in DB):** Corporate spread 1.61 and VIX 16.34. (Postgres; macro)

## Macro and event framing for this week
- **Data availability note:** The macro table currently has incomplete values for several headline releases (inflation, labor, policy rate), so this brief is emphasizing market-implied signals from equities/rates/credit rather than stale or partial macro prints. (Postgres; macro)
- **What to watch this week (qualitative):** US policy communication, labor/consumption updates, and rate-volatility sensitivity remain the highest-probability drivers of cross-asset direction.

## Risk-on / risk-off signal check
- **Current read: Mild risk-off.**
  - Confirmation: broad negative 1D and 1W returns across US style boxes and non-US equities. (Postgres; prices)
  - Counterweight: volatility and credit spread levels are not at stress extremes in current data snapshot. (Postgres; macro)

## Implications for target date / target risk portfolios
1. **Keep equity risk balanced across style buckets:** Growth momentum has softened while value has only marginally outperformed; avoid overconcentrating in any single style sleeve until breadth improves. (Postgres; prices)
2. **Maintain international exposure discipline, but pace additions:** EAFE/EM underperformance over 1M argues for staged rebalancing rather than one-shot increases. (Postgres; prices)
3. **Use the still-positive curve slope as a carry anchor in core fixed income:** With 2s10s at +61 bps, duration can remain strategic, but keep hedges for renewed equity downside. (Postgres; sovereign_yield_curve)
4. **Alternatives/private sleeves:** In a mild risk-off tape, private market marks may lag public repricing; maintain liquidity buffers and avoid forcing tactical shifts off lagged valuation signals.

---
**Coverage note:** Public-database coverage for gold/silver/copper/broad commodities/crypto and private market benchmarks is limited in this environment today; omitted numeric callouts where reliable sourced values were unavailable.