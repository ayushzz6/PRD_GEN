# Advisory recommendation based on Profiling

## Problem Statement

Angel One’s current advisory journey lacks a consistent, regulatory-grade risk profiling of customers, resulting in generic or misaligned recommendations across the diverse recommendation types offered on our app. This gap erodes user trust and conversion, complicates suitability justification and audit trails, and increases compliance exposure under SEBI Investment Advisers Regulations that mandate client risk profiling. Additionally, the absence of an objective, uniform scoring framework for recommendations prevents us from assembling coherent, comparable recommendation baskets aligned to individual risk appetites. As competitors move toward risk-aligned portfolios at onboarding, this shortfall undermines our differentiation and limits the advisory business’s growth potential.

## Goals & Objectives

1. Deliver SEBI-compliant risk profiling at onboarding to accurately determine each client’s risk capacity and appetite for advisory suitability.
2. Personalize recommendation baskets combining both recommendation types offered on the app to align with each client’s profile and goals.
3. Provide transparent, interpretable recommendation scores that build trust and enable informed decision-making.
4. Increase activation and engagement within the advisory journey through high-quality, risk-appropriate basket recommendations.
5. Reduce suitability risks and client complaints by documenting rationale, constraints, and appropriateness for every recommendation.
6. Strengthen monetization of advisory services by improving conversion from profiling to basket adoption and ongoing usage.

## Lead & Lag Metrics

| Metric  |type (Lead/Lag) |
|-----------|-----------|
| Risk profiling completion rate (new advisory onboarding) | Lead |
| Risk-fit alignment rate between user profile and recommended basket | Lead |
| View-to-accept rate for first recommended basket | Lead |
| Time to first recommendation exposure after onboarding (median) | Lead |
| Basket-to-trade conversion rate (within 30 days) | Lag |
| 30-day advisory user retention | Lag |
| Brokerage revenue from basket-driven trades | Lag |

## Target Users / Personas

Below are the most relevant and distinct target user personas for “Advisory recommendation based on Profiling,” calibrated to Angel One’s advisory journey, Indian retail investing reality, and SEBI suitability norms.

1) First-time Equity Investor from Tier 2/3 (“Bharat Beginner”)
- Role/segment: 22–35, new to equities, low financial literacy, small tickets (₹1–10k/month), largely salary-dependent.
- Needs/pain points: Overwhelmed by stock choices; fear of loss; wants simple, low-risk, guided entry; limited time to research.
- Why this benefits them: Risk profiling steers them to conservative baskets (ETFs/large-caps/long-term recos) and away from high-volatility trading ideas. Scored recommendations increase trust and transparency. Meets SEBI suitability to avoid mis-selling.

2) Busy Salaried DIY Investor in Metros
- Role/segment: 25–40, professionals in IT/finance/consulting, moderate risk, invests monthly, time-poor.
- Needs/pain points: Wants quick, credible curation; balanced risk; dislikes hopping between long-term and short-term lists.
- Why this benefits them: Profiling produces blended baskets with a clear long-term vs short-term split aligned to their risk score. Rec-score ranking reduces research time, improving activation and stickiness.

3) Active Trader/Speculator
- Role/segment: 21–35, frequent trader in cash/FO, seeks momentum/intraday/positional setups, high risk tolerance.
- Needs/pain points: Too many signals; wants position sizing guidance and risk controls; hates being throttled by generic “safe” advice.
- Why this benefits them: High-risk profile unlocks trading-heavy baskets with tighter SL/TP rules and higher weight to short-term recommendations. Score-based filtering prioritizes higher-conviction trade ideas while remaining SEBI-compliant on suitability.

4) Long-term Fundamental Wealth Builder
- Role/segment: 30–50, stable income, SIP mentality, prefers large/mid-cap, low-to-moderate risk.
- Needs/pain points: Noise from trading calls; wants low churn and thesis-backed picks; avoids drawdowns.
- Why this benefits them: Profiling suppresses trading ideas and presents investment-only baskets (quality, sectors, factor tilts). Scored recos and basket-level risk explain drawdown expectations, aiding disciplined holding.

5) Affluent/HNI Suitability-sensitive Client
- Role/segment: 35–60, >₹25L/yr income or >₹50L investable, multi-account, often RM-assisted, moderate-to-high capacity but risk-aware.
- Needs/pain points: Requires clear suitability, audit trail, and diversification; seeks transparency to avoid advisor bias; compliance matters.
- Why this benefits them: Documented risk profiling and scored recommendations produce auditable, diversified baskets; facilitates RM-assisted proposals that are SEBI-compliant with rationale and score-backed traceability.

6) Mutual Fund-Only Investor Migrating to Direct Equity
- Role/segment: 28–45, comfortable with SIPs but new to stocks/ETFs; moderate risk with low confidence in security selection.
- Needs/pain points: Wants MF-like simplicity in equities; fears single-stock risk and timing errors.
- Why this benefits them: Profiling offers conservative to balanced equity/ETF baskets with SIP/one-click features. Rec scores offer comfort similar to fund rating systems, easing the MF-to-equity transition and growing wallet share.

7) Derivatives-Curious but Inexperienced User
- Role/segment: 21–35, explores options/futures after social influence; low experience; risk perception is often inflated.
- Needs/pain points: Prone to over-risking; lacks understanding of payoff/risk; needs guardrails.
- Why this benefits them: Profiling gates access to high-risk derivative recommendations; baskets include defined-risk structures (e.g., spreads) only if risk score permits. Score and suitability messaging reduce complaints and losses, aligning with SEBI requirements.

8) Pre-retiree/Retiree Capital Preservation Seeker
- Role/segment: 50–65+, corpus-focused, income/drawdown sensitive, low risk.
- Needs/pain points: Cannot afford large drawdowns; dislikes churn; needs clarity on downside.
- Why this benefits them: Risk profiling channels them to conservative baskets (dividend/defensive/ETF-heavy) with low volatility scores. Transparent rec scoring and expected risk bands support suitability and trust.

9) RM/Partner-Assisted Client (Branch/Authorized Person channel)
- Role/segment: Clients onboarded via Angel One RMs/APs in semi-urban/urban centers; mixed risk/experience.
- Needs/pain points: Inconsistent manual suitability assessment; risk of mis-selling; fragmented advisory artifacts.
- Why this benefits them: Standardized profiling and recommendation scores enable RMs/APs to propose compliant, basketized advice quickly, with logged suitability and rationale—reducing regulatory risk and improving conversion.

10) NRI Investor Using PIS/NRO Routes
- Role/segment: Indians abroad investing intermittently; time-zone constrained; moderate risk; prefers fewer, higher-quality actions.
- Needs/pain points: Hard to monitor markets; needs concise, compliant, executable ideas across time zones.
- Why this benefits them: Profiling crafts low-maintenance, higher-conviction baskets aligned to risk capacity, with rec scores and alerts that prioritize actions—improving engagement and AUM without overtrading.

Why these personas align to the product and Angel One goals
- Directly leverage risk profiling and recommendation scoring to create suitable, blended baskets of our two advisory types (long-term investment calls and short-term trading ideas).
- Address SEBI Investment Adviser regulations on risk profiling, suitability, and auditability—reducing complaints and regulatory exposure.
- Support strategic growth: expand advisory adoption in Tier 2/3, migrate MF users to equities, improve activation for time-poor metros, deepen HNI/RM-assisted share, and responsibly gate derivatives to protect users and brand.

## Functional Requirements and User Stories

| User Story | Functional Requirement |Acceptance Criteria |
|------------|-------------------------|--------------------|
| US-01: As a novice Angel One investor, I want a simple risk questionnaire that outputs my risk score and band, so that the app can tailor a suitable recommendation basket. | FR-01 (maps to US-01) [Must]: Deliver a 10-question risk-profiling flow producing Risk Score (0–100) and Band (Conservative/Moderate/Aggressive). Completion mandatory before showing advisory baskets. Store timestamped responses, consent, and score. [Compliance-sensitive: SEBI, DPDPA] | Given a user completes all questions and checks consent, when they submit, then Risk Score and Band are shown and stored with timestamp. Given consent is unchecked, when they submit, then submission is blocked with an error. Given a completed profile, when entering advisory, then the stored score/band is used. |
| US-02: As an active Angel One day trader, I want my profile to skew baskets toward short-term ideas with clear limits, so that I can deploy capital safely per my risk. | FR-02 (maps to US-02) [Must]: Construct baskets per Risk Band with fixed mixes: Conservative 90% long-term/10% short-term; Moderate 70/30; Aggressive 40/60. Include only ideas with IdeaScore ≥60. Min 8, max 15 ideas. Cap any idea at 15% weight; short-term stop-loss note included. | Given Conservative band, when generating a basket, then mix is 90% long-term/10% short-term with 8–15 ideas and IdeaScore ≥60. Given any idea weight exceeds 15%, when building, then weight is trimmed to 15%. Given short-term ideas are shown, when rendered, then a stop-loss note is displayed. |
| US-03: As an Angel One HNI investor, I want each idea’s score, rationale, and suitability tag, so that I can trust how the basket matches my profile. | FR-03 (maps to US-03) [Should]: Display for each idea: IdeaScore (0–100), score factors, risk label, expected holding period, rationale (<=140 chars), and suitability tag 'Matches your profile' or 'Outside profile'. [Compliance-sensitive: SEBI suitability] | Given basket details, when the user opens any idea, then IdeaScore, factors, risk label, holding period, rationale, and a suitability tag are visible. Given an included idea, when shown, then tag reads 'Matches your profile'. Given an excluded idea in discovery, when shown, then tag reads 'Outside profile'. |
| US-04: As a conservative Angel One retiree, I want to re-take my risk profile and be alerted when suitability changes, so that my basket stays aligned to my situation. | FR-04 (maps to US-04) [Must]: Allow re-profiling anytime. If Risk Band changes, generate new basket proposal and notify. Require explicit user confirm to apply changes. Retain history of past profiles and applied dates. [Compliance-sensitive: SEBI record-keeping] | Given a user re-profiles and band changes, when they finish, then a new basket proposal is created and a notification is sent. Given the user reviews the proposal, when they confirm, then the new basket is applied and old/new profile details are stored. Given the user dismisses, then no changes are applied. |
| US-05: As a KYC-complete salaried Angel One user, I want explicit consent and an audit trail for profiling and advice, so that I can review past suitability decisions. | FR-05 (maps to US-05) [Must]: Apply eligibility guardrails: exclude F&O/leveraged ideas if segment not activated or user opts out. For Conservative or age ≥60, short-term ideas ≤20% and no leveraged instruments. [Compliance-sensitive: SEBI suitability/exchange eligibility] | Given F&O is not activated, when generating baskets, then no F&O/leveraged ideas appear. Given user age ≥60 or Conservative band, when building, then short-term allocation ≤20% and leveraged instruments are excluded. Given the user opts out of derivatives, then all derivative ideas are excluded. |
| US-06: As an existing Angel One customer, I want my known details pre-filled and advice blocked until I finish profiling, so that onboarding is fast and compliant. | FR-06 (maps to US-06) [Should]: Pre-fill profiling with KYC/trading data (age, income, occupation, segments, experience). Allow edit. Block advisory baskets until mandatory questions answered. Save progress on exit. [Compliance-sensitive: DPDPA consent and purpose limitation] | Given a KYC user starts profiling, when the form loads, then age, income, occupation, segments, and experience are pre-filled and editable. Given mandatory questions are unanswered, when user finishes, then an error shows and advisory baskets remain blocked. Given user exits mid-way, when they return, then progress resumes at last step. |
| US-07: As a long-term DIY Angel One investor, I want clear triggers and timely notifications when my basket refreshes, so that I can accept changes confidently. | FR-07 (maps to US-07) [Could]: Refresh basket when: new idea added, any IdeaScore changes by ≥10 points, Risk Band changes, or 30 days pass. Notify within 1 hour; show change diff; apply only after user acknowledges. | Given any included idea’s IdeaScore changes by ≥10, when refresh logic runs, then a refresh is created and the user is notified within 1 hour. Given 30 days since last refresh, when user opens the app, then a scheduled refresh with change summary is available. Given the user declines, then no update is applied. |

## CX Predictions

Pain Points Summary (4–5 concise bullets)| PRD Objective: | Sentiment::
- Pain Point: "The app keeps pushing aggressive stock calls even though I chose ‘low risk’ during signup." | PRD Objective: Obj 1 & 2 — SEBI-compliant risk profiling and personalized baskets aligned to risk | Positive
- Pain Point: "Why is this stock in my basket? I can’t see the risk or how it fits my profile." | PRD Objective: Obj 3 & 5 — Transparent, interpretable scores with documented suitability rationale | Positive
- Pain Point: "Recommendations feel siloed across two sections; I want one basket that mixes them for goals like tax-saving or steady income." | PRD Objective: Obj 2 — Combine both recommendation types into a goal-aligned basket | Positive
- Pain Point: "I’m worried these suggestions aren’t SEBI-compliant for my situation; support couldn’t explain suitability." | PRD Objective: Obj 1 & 5 — Robust onboarding risk assessment and clear appropriateness documentation | Positive
- Pain Point: "Please don’t make me fill a long risk questionnaire—I drop off if onboarding takes more than a minute." | PRD Objective: Obj 1 — Risk profiling at onboarding may add friction; needs to be concise/adaptive | Negative

Final Sentiment Analysis: Positive: 4 | Negative: 1

## Competitors

Below is a focused competitor analysis for “Advisory recommendation based on profiling,” centered on onboarding risk profiling, risk-aligned recommendation baskets (stocks/ETFs; research/advisory types), and per-recommendation scoring/rating signals that can be used to construct baskets.

Competitor insights (concise and actionable)
- Zerodha
  - Relevance: Provides risk-based portfolios via smallcase (partners run onboarding with risk questions and map users to low/moderate/high risk portfolios). No Zerodha-native advisory personalization.
  - Basket coverage: Thematic/goal-based stock and ETF baskets; periodic rebalancing; clear volatility/risk labels at portfolio level.
  - Scoring signals: Portfolio-level risk/volatility labels and factsheets; no unified in-app, per-recommendation score within Zerodha itself.
  - Actionable takeaway for Angel One: Build an integrated, Angel-native risk profiler and a unified scoring model surfaced across both Angel and partner advisories to avoid the current Zerodha-style fragmentation.

- Upstox
  - Relevance: Offers smallcase integration; no unified, app-wide suitability gating for all recommendations.
  - Basket coverage: Risk-bucketed smallcases; “Smartlists” are curated lists but not risk-profile-driven.
  - Scoring signals: Limited visible per-stock scoring across the app; relies on third-party portfolio labels for risk, not a broker-native score.
  - Actionable takeaway: Differentiate with a single risk profile that drives all recs and basket construction plus transparent, comparable scores per idea.

- Groww
  - Relevance: Stock baskets via smallcase; MF journey shows SEBI Riskometer and basic suitability cues; limited broker-native risk profiling across the entire advisory surface.
  - Basket coverage: Thematic and risk-labeled baskets; MF and equity journeys are separate.
  - Scoring signals: MF risk labels; no consistent per-stock/strategy score displayed across advisory.
  - Actionable takeaway: Provide cross-asset (stocks/ETFs and MF) suitability with one risk profile and a common scoring fabric.

- ICICI Direct
  - Relevance: Strong advisory stack with “One Click Portfolios” aligned to risk bands (Conservative/Moderate/Aggressive). Advisory/Prime services capture client suitability and risk.
  - Basket coverage: Model portfolios with stock/ETF mixes; periodic rebalancing; goal/risk categorization.
  - Scoring signals: Research ratings and suitability tags at portfolio/idea level; not a single numeric score unified across all ideas.
  - Actionable takeaway: Match breadth of risk buckets, but outdo on transparency via a normalized scoring framework across both short-term ideas and long-term baskets.

- HDFC Securities
  - Relevance: Investment advisory (RIA) flow includes risk profiling; distributes thematic/risk-labelled baskets (incl. smallcase/WealthDesk integrations) plus in-house research.
  - Basket coverage: Equity/ETF baskets with stated risk; rebalancing and factsheets.
  - Scoring signals: Risk/suitability labels and allocation guidance; no ubiquitous per-idea numeric scoring across the app.
  - Actionable takeaway: Angel can win with a single scoring rubric per recommendation and automatic basket assembly tied to the user’s risk score.

- Sharekhan
  - Relevance: Sharekhan NEO (robo-advisory for MFs) captures risk profile and builds portfolios; equity model portfolios exist alongside research calls.
  - Basket coverage: MF portfolios via NEO and equity model portfolios; scheduled reviews.
  - Scoring signals: MF risk/ratings; equity side uses research rationales rather than a cross-surface score.
  - Actionable takeaway: Unify multi-product advice under one risk profile and present a comparable score per idea to drive basket formation.

- 5paisa
  - Relevance: Strong quant-style front end—Smart Investor/Scorecards with factor-based signals (e.g., valuation, earnings quality, momentum) influencing recommendations; also offers smallcase/WealthDesk baskets.
  - Basket coverage: Thematic/model baskets plus factor-led stock shortlists.
  - Scoring signals: Multi-factor “scorecards” at the stock level prominently used to drive recs.
  - Actionable takeaway: Match or exceed factor transparency and use the per-idea score to programmatically compose and rebalance risk-aligned baskets.

- Motilal Oswal
  - Relevance: Advisory and wealth offerings capture risk profile; runs model/thematic portfolios and discretionary advisory with periodic rebalancing.
  - Basket coverage: Equity/ETF model portfolios mapped to risk/goal; strong research depth.
  - Scoring signals: Research ratings and portfolio risk tags; less emphasis on a consistent numeric score across all recs.
  - Actionable takeaway: Deliver a clearer, quant-backed per-idea score and auto-construct baskets that blend tactical and long-term recommendations per user risk.

At-a-glance summary
| Competitor | Related product features as per title and description |
|-------------|--------------------|
| Zerodha | - Risk-based portfolios via smallcase with onboarding risk Q&A and low/moderate/high mapping. - Thematic stock/ETF baskets with volatility/risk labels and rebalancing. - No Zerodha-native, per-recommendation scoring; risk personalization exists mainly within partner flows. |
| Upstox | - smallcase integration; no unified app-wide risk-profiling that gates all advisory. - Curated “Smartlists” but not personalized by risk. - Limited visible per-idea scoring; depends on third-party portfolio risk tags. |
| Groww | - smallcase stock baskets; MF Riskometer shown in MF flow. - Risk/thematic baskets discoverable but not driven by a single user risk profile across products. - No consistent per-recommendation score across advisory. |
| ICICI Direct | - “One Click Portfolios” segmented by risk (Conservative/Moderate/Aggressive) with periodic rebalancing. - Advisory/Prime services capture client risk and suitability. - Research ratings/suitability tags, though not a single numeric score applied across all recommendations. |
| HDFC Securities | - Advisory (RIA) onboarding with risk profiling. - Thematic/risk-labelled baskets (incl. smallcase/WealthDesk) and in-house model portfolios. - Portfolio risk labels and allocation guidance; no ubiquitous per-idea numeric scoring. |
| Sharekhan | - NEO robo-advisory for MFs uses risk profiling to construct portfolios. - Equity model portfolios alongside research calls. - MF risk/ratings present; equity ideas not consistently scored across the app. |
| 5paisa | - Factor-driven Smart Investor/Scorecards inform stock ideas (e.g., valuation, earnings quality, momentum signals). - smallcase/WealthDesk baskets available. - Clear per-stock factor scoring used in recommendations; closer to the “score-based basket” vision. |
| Motilal Oswal | - Risk profiling in advisory/wealth journeys; discretionary and non-discretionary offerings. - Model/thematic portfolios with periodic rebalancing mapped to risk/goal. - Research ratings and portfolio risk tags; less emphasis on a uniform numeric score per recommendation. |

How this informs Angel One’s strategy for the new feature
- Build a single, compliant risk-profiling onboarding that drives all advisory surfaces (Angel in-house and partner-led), unlike most rivals’ fragmented experiences.
- Operationalize a transparent, factor-based per-recommendation score (e.g., quality, valuation, momentum, risk/volatility, liquidity), surfaced alongside each idea and used to auto-assemble risk-aligned baskets spanning both recommendation types on our app.
- Offer dynamic basket rebalancing tied to the user’s profile and market drift, with guardrails (SEBI suitability, concentration/risk caps) and clear disclosures—an area where discount brokers relying on third parties are weaker.
- Ensure cross-asset consistency (stocks and ETFs at launch; extensible to MF/FO later) so the profile and score travel with the user across the advisory journey.

## Risks & Dependencies

1. Regulatory & Compliance Risk – SEBI IA Risk Profiling & Suitability Breach: The onboarding questionnaire and scoring may not adequately capture “risk appetite and capacity,” leading to unsuitable recommendation baskets for clients. SEBI IA Regulations 2013, Reg. 16: “Investment advisers shall ensure that a proper risk-profile of the client is undertaken, including the client’s risk appetite and capacity.” Reg. 17 mandates suitability of advice based on that profile. Any mismatch between basket risk and the client’s profile can trigger regulatory action and client harm.

2. Regulatory & Compliance Risk – SEBI IA Recordkeeping/Audit Trail Gaps: Missing, mutable, or unversioned logs of the client questionnaire, computed risk score, basket composition, and rationale per client can fail SEBI inspections. IA Regulations require maintaining records of risk profiling, advice, and rationale for a minimum period (commonly interpreted as five years). Without immutable, time-stamped artifacts, Angel One cannot evidence suitability.

3. Regulatory & Compliance Risk – UPSI/Chinese Wall Break in Scoring: Using non-public data (e.g., internal order flow, unpublished research views, or corporate access insights) as features for recommendation scoring could be construed as use of UPSI, breaching insider trading and research/advisory separation expectations. Any contamination of models or workflows with UPSI exposes Angel One to enforcement and reputational risk.

4. Technical Risk – Model Drift/Score Instability: The recommendation-scoring model can drift under changing market regimes (e.g., volatility spikes), misclassifying instruments and over-allocating high-beta/leveraged products to conservative profiles. Lack of ongoing backtests, PSI/KS monitoring, and versioned models can cause silent degradation and widespread mis-suitability.

5. Technical Risk – Latency/Partial Failure in Basket Assembly: Cross-service calls (profiling service, instrument-risk service, research APIs) may exceed p95 > 1s or fail partially, yielding inconsistent basket constituents or missing exclusions (e.g., leverage caps). Without idempotency and consistency checks, the user may see and act on a basket that violates their disclosed risk limits.

6. Operational Risk – Stale/Incomplete Client Data in Profiling Pipeline: ETL/stream failures, delayed KYC updates, or missing financial goal/income data can default clients to incorrect profiles or skip mandatory suitability gates. This leads to incorrect basket generation, higher complaint rates, and exposure to regulatory findings on suitability.

7. Business Risk – Conflicts of Interest Biasing Basket Composition: Revenue incentives (brokerage, partner fees, margin/FO exposure) can bias the scoring or thresholds to over-recommend higher-margin instruments to low/moderate risk clients. This creates conduct risk (suitability breach), erodes trust, and increases attrition and regulatory complaints.

8. Security Risk – DPDPA Personal Data Exposure via Logs/SDKs: Risk-profiling data (financial goals, income, dependents) may leak via verbose logs, analytics SDKs, or misconfigured data lakes; retention beyond declared periods or secondary use (e.g., marketing derivatives) violates DPDPA. DPDPA 2023 requires valid consent, purpose limitation, and honoring data principal rights (access/erasure). Any breach or misuse invites penalties and mandatory breach notifications.


At-a-glance summary (for PRD inclusion)
| ID | Category                      | Risk (specific)                                                | Primary impact                                 | Regulatory basis (if any)                                  |
|----|-------------------------------|----------------------------------------------------------------|------------------------------------------------|------------------------------------------------------------|
| 1  | Regulatory & Compliance       | SEBI IA risk profiling/suitability breach                      | Unsuitable baskets; enforcement risk           | SEBI IA Regs 2013, Reg. 16–17                              |
| 2  | Regulatory & Compliance       | Missing/weak audit trail of advice and rationale               | Inspection failure; penalties                  | SEBI IA Regs (recordkeeping requirements)                  |
| 3  | Regulatory & Compliance       | UPSI/Chinese wall breach in scoring features                   | Insider trading exposure; reputational damage  | Insider trading prohibitions; RA/IA separation expectations|
| 4  | Technical                     | Model drift/score instability under regime change              | Mis-suitability at scale                       | —                                                          |
| 5  | Technical                     | Latency/partial failures in basket assembly microservices      | Inconsistent/unsafe basket shown to users      | —                                                          |
| 6  | Operational                   | Stale/incomplete client data in profiling pipeline             | Wrong profile; higher complaints               | —                                                          |
| 7  | Business                      | Incentive bias toward high-margin/leveraged instruments        | Conduct risk; churn; brand damage              | —                                                          |
| 8  | Security                      | DPDPA personal data exposure via logs/SDKs/over-retention      | Regulatory penalties; breach notifications     | DPDPA 2023 (consent, purpose limitation, data rights)      |