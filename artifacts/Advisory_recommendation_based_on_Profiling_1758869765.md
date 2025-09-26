# Advisory recommendation based on Profiling

## Problem Statement

Angel One’s current advisory journey lacks a standardized, auditable risk-profiling mechanism and a consistent way to assess the relative risk and suitability of individual recommendations, resulting in generic and fragmented guidance across both recommendation modalities on the app. This undermines customer trust and engagement, prevents us from presenting coherent, risk-aligned baskets of ideas, and constrains adoption and monetization of advisory offerings. The gap also increases regulatory exposure, as SEBI Investment Adviser Regulations require documented client risk profiling and suitability assessment. In a market where investors expect risk-aligned portfolios from competitors, this deficiency places Angel One at a competitive disadvantage.

## Goals & Objectives

1. Launch a SEBI-compliant, intuitive risk-profiling onboarding that segments customers and powers personalized advisory baskets across all advisory categories on the app.
2. Deliver explainable, score-based recommendations that transparently justify basket composition, strengthening investor trust and market differentiation.
3. Increase adoption and engagement of advisory by matching risk profiles with suitable recommendation baskets that drive better outcomes and reduce churn.
4. Enhance regulatory readiness with auditable profiling records and recommendation rationales, reducing mis-selling risks and support costs.
5. Expand monetization through tiered access to curated baskets and premium advisory experiences aligned to customer risk tiers and lifecycle needs.
6. Enable cross-channel consistency by using a unified risk score to coordinate portfolio nudges, alerts, and advisor interactions across app, web, and partner platforms.

## Lead & Lag Metrics

| Metric  |type (Lead/Lag) |
|-----------|-----------|
| Risk profiling onboarding completion rate (eligible advisory users) | Lead |
| Recommendation basket adoption rate (users acting on a recommended basket post-onboarding) | Lead |
| Alignment rate: % of users whose basket risk score matches their profiling risk band | Lead |
| CTR to recommended basket details from onboarding completion | Lead |
| Revenue attributable to executed recommendations from recommended baskets per user | Lag |
| 30/90-day retention of advisory users who completed profiling | Lag |
| Reduction in suitability-related complaints/opt-outs related to recommendations | Lag |
| Risk-adjusted performance of recommended baskets vs benchmark (30/90 days) | Lag |

## Target Users / Personas

Below are the prioritized target user personas for “Advisory recommendation based on Profiling,” aligned to Angel One’s advisory journey, India market realities, and SEBI suitability/risk-profiling requirements.

1) New-to-investing Retail (Tier-2/3, first-time equity/MF entrants)
- Needs/pain: Low financial literacy, fear of loss, decision overload; wants simple, “safe” ways to start.
- Why this helps: Risk-based onboarding steers them to conservative, easy-to-understand baskets (large-caps/ETFs, no F&O), with scored recommendations that reduce guesswork and mis-buying; aligns with SEBI suitability mandates.

2) Time-poor Salaried Professional (Metro, 10k–50k/month investing)
- Needs/pain: Wants long-term compounding with occasional tactical ideas but lacks time and curation.
- Why this helps: Profile-driven baskets mix long-term research ideas with capped tactical trades sized to their risk; per-idea scores and position-sizing cut noise and improve adherence; auditable suitability for compliance.

3) Aggressive Derivatives Trader (Young, F&O/intraday/swing active)
- Needs/pain: Over-leverage, drawdowns, inconsistent risk control; needs structured exposure and better signal quality.
- Why this helps: Onboarding gates risk capacity before surfacing high-risk calls; scored recommendations with margin/VAR impact and hedged basket templates enforce discipline; reduces complaints/mis-selling risk.

4) Goal-based Family Steward (30–45, planning education/home goals)
- Needs/pain: Scattered advice, can’t translate goals into risk and product mix; wants measured upside without nasty drawdowns.
- Why this helps: Risk profiling converts goals and horizons into moderate-risk baskets blending quality equities/ETFs and limited tactical ideas; scores and projected drawdown bands set expectations and meet suitability norms.

5) Pre-retiree/Retiree Capital Preserver (50+, low risk tolerance)
- Needs/pain: Capital protection and steady income; wants to avoid speculative content and surprises.
- Why this helps: Profiling suppresses high-risk instruments and surfaces conservative baskets; recommendation scores, risk labels, and suitability logs provide clarity for a vulnerable segment under SEBI oversight.

6) NRI India-Equity Seeker (US/GCC/UK-based, FEMA-compliant)
- Needs/pain: Time-zone constraints, limited product access, wants low-touch, compliant exposure.
- Why this helps: Risk-based onboarding tailors to permissible products and time-zone friendly baskets; scored recommendations and periodic rebalancing reports make oversight easy and compliant.

7) Affluent/HNI Diversifier (≥1 Cr net worth, multi-account)
- Needs/pain: Diversification, tax efficiency, risk caps, wants transparency and control across strategies.
- Why this helps: Advanced profile parameters (capacity, concentration limits) drive multi-basket allocations across long-term and tactical ideas; per-idea scoring and audit trails support internal controls and SEBI suitability.

8) Advisory Subscription Buyer (pays for research/model portfolios)
- Needs/pain: Trust and measurable performance; wants to know “why this idea” and “how risky.”
- Why this helps: Recommendation-level scoring, rationale, and basket fit improve transparency and retention; profiling ensures subscribers only see suitable ideas, reducing refunds/escalations.

9) DIY Thematic/Small-ticket Investor (Gen Z/millennial, 2k–10k/month)
- Needs/pain: Wants trending themes but risks over-concentration and impulse buys.
- Why this helps: Profiling caps risk and sizes bets within thematic baskets; scores temper hype with quality signals, aligning discovery with suitability and long-term habit formation.

10) Internal – Research/Advisory Analyst (Angel One)
- Needs/pain: Inconsistent risk labels across ideas; hard to map ideas to client suitability at scale.
- Why this helps: A standardized scoring framework per recommendation enables automated basket construction by client risk tier; reduces post-trade escalations and improves research accountability.

11) Internal – Compliance/RM/Support (Angel One)
- Needs/pain: Must evidence suitability and avoid mis-selling; handle grievances with clear audit trails.
- Why this helps: Stored risk profiles, idea scores, and recommendation-to-profile mapping create defensible, SEBI-compliant journeys; faster resolution and lower regulatory risk.

Why these personas are right for this product
- They mirror core Indian market segments Angel One serves (new investors, traders, salaried professionals, NRIs, HNIs) and internal operators essential to delivery.
- Each segment’s pain is directly addressed by risk-based onboarding and scored recommendations, enabling suitable, mixed-type baskets (long-term research + short-term/trading) and measurable outcomes.
- They support strategic goals: expand advisory adoption, reduce churn/complaints, enable cross-sell of higher-value advisory, and maintain SEBI-compliant suitability across the funnel.

## Functional Requirements and User Stories

| User Story | Functional Requirement |Acceptance Criteria |
|------------|-------------------------|--------------------|
| US-01: As a novice investor using Angel One Advisory for the first time, I want a short, plain-language risk profiling, so that I only see baskets that match my comfort level. | FR-01 (maps to US-01) [Priority: Must] [Compliance-sensitive: SEBI IA Regulations]: Show an 8–12 question profiler (attitude + capacity) in onboarding. Output a Risk Profile Score (RPS) 1–100 and band (Conservative/Moderate/Aggressive). Hide recommendations until completion and display RPS and band summary. | - Given an unprofiled advisory user, when they start onboarding, then they see 8–12 questions. - Given the user submits all answers, when scoring completes, then RPS (1–100) and band are shown. - Given the profile is incomplete, when opening recommendations, then a “Complete risk profile to proceed” blocker is shown. |
| US-02: As an active intraday trader, I want my aggressive tolerance reflected in baskets, so that I get more trading recommendations while staying within defined risk limits. | FR-02 (maps to US-02) [Priority: Should]: For Aggressive band (RPS ≥67), default baskets must include both types, with 40–60% trading recommendations by weight. Cap any single high-risk item (RecRS >80) at ≤20% of basket weight. | - Given a user with RPS=80, when viewing the default basket, then trading recommendations are 40–60% of total weight and at least one long-term idea exists. - Given an item with RecRS=85, when included in the basket, then its weight is ≤20%. |
| US-03: As an HNI (portfolio > ₹50L), I want my financial capacity considered, so that the risk profile is not based only on attitude. | FR-03 (maps to US-03) [Priority: Must] [Compliance-sensitive: SEBI IA Regulations]: Collect optional capacity inputs (annual income, net worth, liquid surplus) and weight them as 40% of RPS. If absent, set capacity subscore=33. Show attitude vs capacity breakdown in the RPS screen. | - Given capacity inputs are provided, when saving the profile, then RPS shows “capacity contribution (40%)” numerically. - Given no capacity inputs, when saving the profile, then capacity subscore=33 and “assumed conservative capacity” is displayed and logged. |
| US-04: As a salaried SIP investor whose circumstances change, I want to reprofile and refresh my basket, so that my recommendations stay suitable. | FR-04 (maps to US-04) [Priority: Should]: Allow re-profiling on demand. On submission, regenerate baskets within 5 seconds. Maintain versioned history (timestamp, old RPS, new RPS, band). Allow one-click revert to previous profile within 7 days. | - Given an existing RPS, when the user reprofiles and submits, then new baskets are generated within 5 seconds and a history entry is created. - Given a reprofile within 7 days, when the user taps “Revert,” then the prior RPS and baskets are restored. |
| US-05: As a compliance-conscious investor, I want to see each recommendation’s risk score and suitability, so that I can avoid unsuitable picks or explicitly acknowledge them. | FR-05 (maps to US-05) [Priority: Must] [Compliance-sensitive: SEBI IA Regulations]: Each recommendation must have and display a Recommendation Risk Score (RecRS 1–100) and a one-line suitability rationale. Block selection if RecRS exceeds the user’s band maximum unless the user acknowledges; log overrides. | - Given a Conservative band (max=66), when the user tries to add an item with RecRS=75, then a modal shows risk mismatch and “Proceed/Cancel.” - Given the user proceeds, when confirmed, then an override log (user, item, timestamp) is recorded. - Given any recommendation card, when displayed, then RecRS and a rationale are visible. |
| US-06: As a SIP-first investor, I want my basket to combine long-term and trading ideas aligned to my risk band, so that I get a balanced, suitable portfolio. | FR-06 (maps to US-06) [Priority: Must]: The basket engine must keep weighted-average RecRS within the user’s band midpoint ±5 and include both types with splits: Conservative 90/10, Moderate 70/30, Aggressive 50/50 (long-term/trading) ±5% tolerance. | - Given a Moderate band user, when viewing the basket, then weighted-average RecRS is 45–55 and the split is 65–75% long-term and 25–35% trading. - Given an Aggressive band user, when viewing the basket, then weighted-average RecRS is 78–88 and the split is 45–55% each type. |
| US-07: As a privacy-conscious user, I want explicit control over profiling consent, so that my data is used lawfully and I can withdraw it anytime. | FR-07 (maps to US-07) [Priority: Must] [Compliance-sensitive: DPDPA 2023]: Obtain explicit consent for profiling with purpose and retention notice. Allow consent withdrawal anytime. On withdrawal, disable recommendations immediately and delete profiling data within 7 days; provide confirmation. | - Given consent is denied, when starting profiling, then the flow stops and advisory recommendations are disabled. - Given consent is withdrawn, when requested, then recommendations are disabled immediately and a deletion confirmation is available within 7 days. |

## CX Predictions

- Pain Points Summary (4–5 concise bullets):
  - Pain Point: "Generated: The advisory picks don’t match my risk comfort—too many high-risk bets for a beginner." | PRD Objective: 3 – Match risk profiles with suitable baskets to improve outcomes. | Sentiment: Positive
  - Pain Point: "Generated: I see a list of stocks/funds but no clear reason or score—why were these chosen for me?" | PRD Objective: 2 – Explainable, score-based recommendations and basket rationale. | Sentiment: Positive
  - Pain Point: "Generated: App says hold, web nudges me to rebalance—advice is inconsistent across channels." | PRD Objective: 6 – Unified risk score to align nudges and advice across channels. | Sentiment: Positive
  - Pain Point: "Generated: Please don’t make me fill a 20-question survey—onboarding is already tiring." | PRD Objective: 1 – New risk-profiling onboarding must be intuitive to avoid friction. | Sentiment: Negative
  - Pain Point: "Generated: Don’t lock the good baskets behind a paywall unless I can try and see value first." | PRD Objective: 5 – Tiered monetization of curated baskets; risk of perceived paywalling. | Sentiment: Negative

- Current PRD Objectives Covered:
  - Objective: Launch a SEBI-compliant, intuitive risk-profiling onboarding that segments customers and powers personalized advisory baskets across all advisory categories on the app. | Related Pain Points: "Generated: Please don’t make me fill a 20-question survey—onboarding is already tiring." | Sentiment Impact: Negative
  - Objective: Deliver explainable, score-based recommendations that transparently justify basket composition, strengthening investor trust and market differentiation. | Related Pain Points: "Generated: I see a list of stocks/funds but no clear reason or score—why were these chosen for me?" | Sentiment Impact: Positive
  - Objective: Increase adoption and engagement of advisory by matching risk profiles with suitable recommendation baskets that drive better outcomes and reduce churn. | Related Pain Points: "Generated: The advisory picks don’t match my risk comfort—too many high-risk bets for a beginner." | Sentiment Impact: Positive
  - Objective: Expand monetization through tiered access to curated baskets and premium advisory experiences aligned to customer risk tiers and lifecycle needs. | Related Pain Points: "Generated: Don’t lock the good baskets behind a paywall unless I can try and see value first." | Sentiment Impact: Negative
  - Objective: Enable cross-channel consistency by using a unified risk score to coordinate portfolio nudges, alerts, and advisor interactions across app, web, and partner platforms. | Related Pain Points: "Generated: App says hold, web nudges me to rebalance—advice is inconsistent across channels." | Sentiment Impact: Positive

- Sentiment Analysis:
  - Positive Points: 3
  - Negative Points: 2

## Competitors

Below is a focused competitor analysis for “Advisory recommendation based on Profiling” specific to Indian broking/advisory products that map user risk profiles to curated recommendation baskets and use scoring to build/justify those baskets.

1) ICICI Direct
- One Click Portfolios: Pre-built stock/ETF baskets mapped to risk buckets (e.g., conservative, moderate, aggressive), with minimum investment, SIP-in-basket, backtests, and scheduled rebalancing.
- Research scoring overlay: ICICIdirect research ratings on each constituent; portfolio-level risk/volatility tags to match client profile.
- Action for Angel One: Match the depth of basket metadata (risk label, min ticket, backtest) and enable 1-tap rebalance acceptance.

2) HDFC Securities
- HDFC Stock Baskets via smallcase: Risk-labelled portfolios (volatility tags like low/medium/high), SIP, and rebalance notifications; easy mapping from user profile to basket type.
- Advisory risk profiler in onboarding (SEBI-compliant) used to guide MF/equity allocations and basket selection.
- Action for Angel One: Mirror seamless handoff from risk quiz to a short, ranked list of baskets with volatility labels and SIP.

3) Motilal Oswal
- MO Model Portfolios: Research-backed baskets (e.g., large-cap compounders, mid-cap focused) with target weights, periodic rebalancing, and risk classification.
- Scoring framework: QGLP-style (Quality-Growth-Longevity-Price) stock evaluation shared in research notes; portfolio-health checks in app.
- Action for Angel One: Expose a transparent, factor-based scoring (e.g., QGLP/Quality-Value-Momentum) at stock and basket levels to build trust.

4) 5paisa
- Smart Investor/Research 360: Stock scorecards (e.g., Quality, Valuation, Momentum, Financial Trend) rolled up into an overall score; used to assemble ready-made portfolios.
- Model portfolios and smallcases with risk labels and 1-click execution/rebalancing for subscribers.
- Action for Angel One: Provide a visible per-recommendation composite score and allow users to sort/filter baskets by that score.

5) IIFL Securities
- Expert/Model Portfolios: Curated equity baskets grouped by risk buckets; min investment, backtested performance, and rebalance alerts.
- smallcase integration with volatility/risk tags and SIP; basic risk profiling in onboarding to map users to appropriate baskets.
- Action for Angel One: Offer goal/risk-aligned baskets plus transparent performance attribution and rebalance discipline.

6) Zerodha
- smallcase on Zerodha: Risk-tagged, theme/strategy-based baskets with volatility labels, SIP, backtests, and rebalance notifications.
- Note: No proprietary equity advisory inside Kite; relies on partner ecosystem for risk-based baskets.
- Action for Angel One: Differentiate by owning the risk-profiler-to-basket mapping natively (not only via partners) and by unifying scoring across all in-app recommendations.

7) Upstox
- smallcase integration: Curated, risk-labelled portfolios with SIP and rebalancing; discovery via themes and volatility filters.
- Curated lists/collections for equities; option strategies carry risk level tags (separate domain).
- Action for Angel One: Provide a single risk score that spans equity baskets (and, if applicable, trading strategies) to keep advice consistent across product types.

8) Kotak Securities
- Stock baskets (incl. via smallcase): Risk/volatility tags, min ticket size, SIP-in-basket, and periodic rebalances; discovery by themes and risk.
- Advisory flows collect risk preferences and map to suitable baskets.
- Action for Angel One: Optimize onboarding to 60–90 seconds and immediately surface 2–3 “best fit” baskets with clear trade-offs (risk, CAGR, drawdown).

At-a-glance summary

| Competitor |Related product features as per title and description|
|-------------|--------------------|
| ICICI Direct | One Click Portfolios mapped to risk buckets; research ratings per stock; min ticket, SIP, backtests, scheduled rebalancing; portfolio risk/volatility tags to align with user profile. |
| HDFC Securities | smallcase-powered risk-labelled baskets (low/med/high volatility), SIP, rebalance notifications; SEBI-compliant risk profiler in onboarding that routes users to suitable baskets. |
| Motilal Oswal | MO Model Portfolios with target weights and risk classification; factor/scoring framework (QGLP) visible in research; portfolio health checks to justify recommendations. |
| 5paisa | Smart Investor/Research 360 stock scoring (Quality/Valuation/Momentum/Trend) aggregated to overall score; expert/model portfolios and smallcases with risk labels and 1-click rebalance. |
| IIFL Securities | Expert/Model Portfolios by risk bucket with min investment and backtests; smallcase integration with volatility tags and SIP; basic in-app risk profiling to map to baskets. |
| Zerodha | smallcase integration delivers risk-based baskets with volatility labels, SIP, backtests, and rebalancing; no proprietary advisory mapping inside Kite. |
| Upstox | smallcase-ready risk-labelled portfolios; curated lists/collections for discovery; options strategies show risk tags (separate), limited native equity advisory personalization. |
| Kotak Securities | Stock baskets (incl. smallcase) with risk/volatility tags, min ticket size, SIP, and periodic rebalances; risk preference collection in advisory flows to map to baskets. |

## Risks & Dependencies

Below are the specific, product-aligned risks for “Advisory recommendation based on Profiling,” categorized as requested. Each item is unambiguous and tied to how Angel One’s risk-profiling onboarding and recommendation-basket scoring will work.

1. Regulatory & Compliance Risk – SEBI IA Risk Profiling and Suitability Breach
Description: The onboarding risk questionnaire and basket-construction logic may fail to capture and use both risk appetite and risk capacity (e.g., income, liabilities, time horizon), resulting in unsuitable recommendation baskets. This includes stale profiles being used to generate baskets after material life/market changes or opaque scoring unable to demonstrate suitability for each recommendation in the basket.
Grounding excerpt: SEBI Investment Advisers Regulations require “a proper risk-profile of the client… including the client’s risk appetite and capacity,” and advice to be suitable to that profile.

2. Regulatory & Compliance Risk – DPDPA Consent, Notice, and Purpose Limitation Failure
Description: Profiling responses, computed risk scores, and recommendation suitability rationales constitute personal data. If onboarding collects or processes these without a compliant, granular consent and clear notice (purpose, processing, withdrawal) or continues processing after consent is withdrawn, Angel One risks DPDPA non-compliance.
Grounding excerpt: DPDPA requires consent to be “free, specific, informed, unconditional and unambiguous with a clear affirmative action,” with notice of “the personal data to be processed and the purpose,” and a right to withdraw consent.

3. Regulatory & Compliance Risk – SEBI Record-Keeping, Audit Trail, and RA/IA Segregation Gaps
Description: If we cannot produce a tamper-evident audit trail that ties each basket recommendation to the client’s current risk profile and a timestamped scoring/version of the model, we risk failing SEBI IA record-keeping/audit requirements. Additionally, if advisory is not operationally segregated from broking/distribution (e.g., incentives, pay, UI nudge), Angel One risks conflict-of-interest violations.
Grounding excerpt: SEBI IA Regulations mandate maintaining records (including risk profiling and suitability) for a minimum period (commonly five years) and require conflict-of-interest controls and appropriate disclosures.

4. Technical Risk – Model/Label Drift Causing Mis-Suitability
Description: The recommendation-scoring model, risk-bucket thresholds, or instrument risk labels can drift with market regime shifts (e.g., changing volatility) or data drift (e.g., new instruments), causing “Moderate” users to receive “Aggressive” baskets or vice versa. Silent drift undermines suitability and auditability.

5. Technical Risk – Scoring/Profiling Service Latency or Outage
Description: If risk-scoring APIs or feature pipelines are slow or down during onboarding or basket retrieval, the app may fallback to stale scores or show no baskets, leading to wrong advice or abandoned journeys. Caching stale profiles post significant events (e.g., income change) is particularly risky.

6. Operational Risk – Instrument Mis-Tagging and Catalog Version Mismatch
Description: If research ops or product teams mis-tag instruments’ risk levels or publish recommendation lists not synchronized with the scoring engine’s version, baskets can combine incompatible recommendations (e.g., derivatives tagged “Moderate”). This creates unsuitable portfolios despite compliant questionnaires.

7. Security Risk – Personal Data Breach or Internal Misuse of Risk Profiles
Description: Profiling responses, computed risk scores, and suitability rationales are high-sensitivity financial inferences. Unauthorized access (internal or external), inadequate segregation from trading data, or insufficient encryption/monitoring could lead to identity-proofing risks, targeted scams, regulatory penalties, and reputational harm.

8. Business Risk – Liability and Reputational Damage from “Implied Assurance” or Misaligned Incentives
Description: If UI copy, nudges, or partner campaigns imply assured returns or push higher-risk baskets to drive revenue (e.g., higher brokerage), customer harm, complaints, regulatory action, and brand damage may ensue. Even a small pattern of complaints around “advice mismatch” can materially impact NPS and regulatory scrutiny.

At-a-glance table

| # | Category                      | Risk Name                                           | Specific Impact on this Product                                                                                           | Compliance Excerpt/Source |
|---|-------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------|
| 1 | Regulatory & Compliance       | SEBI IA Risk Profiling & Suitability Breach         | Incomplete/stale risk inputs or opaque scoring lead to unsuitable baskets; cannot evidence suitability per recommendation | SEBI IA: “proper risk-profile… including risk appetite and capacity” and suitability requirement |
| 2 | Regulatory & Compliance       | DPDPA Consent, Notice & Purpose Limitation Failure  | Profiling without valid consent/notice or processing after withdrawal; unlawful use of risk scores                         | DPDPA: consent “free, specific, informed, unconditional and unambiguous…”; notice of data and purpose; right to withdraw |
| 3 | Regulatory & Compliance       | SEBI Record-Keeping & RA/IA Segregation Gaps        | Missing tamper-evident audit trails (profile → score → basket), or conflicts between advisory and broking/distribution     | SEBI IA: maintain records (incl. risk profiling/suitability) for min. five years; conflict-of-interest controls |
| 4 | Technical                     | Model/Label Drift Causing Mis-Suitability           | Drifted thresholds/labels misclassify risk; “Moderate” users receive “Aggressive” baskets; auditability deteriorates       | —                         |
| 5 | Technical                     | Scoring/Profiling Service Latency or Outage         | Fallback to stale risk scores or empty baskets during onboarding; abandoned journeys or unsuitable advice                   | —                         |
| 6 | Operational                   | Instrument Mis-Tagging & Catalog Version Mismatch   | Mismatched research catalog vs. scoring engine versions create incompatible basket compositions                           | —                         |
| 7 | Security                      | Personal Data Breach/Misuse of Risk Profiles        | Exposure of profiling responses, risk scores, and suitability notes; regulatory penalties and loss of trust                | DPDPA: “reasonable security safeguards to prevent personal data breach” |
| 8 | Business                      | Liability/Reputation from Implied Assurance/Incentives | Perception of assured returns or revenue-driven pushing of high-risk baskets; complaints, fines, brand damage             | SEBI IA: no assured returns; disclose conflicts (industry expectation under IA framework) |

Notes:
- The SEBI IA references pertain to the Investment Advisers Regulations, 2013 (as amended, incl. 2020), notably on risk profiling, suitability, record-keeping, and conflict-of-interest controls.
- DPDPA references pertain to consent, notice, withdrawal, and security safeguard obligations applicable to profiling/risk scoring data.