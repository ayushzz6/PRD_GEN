
PROBLEM_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "You are a senior Product Manager at Angel One.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "Task: Write a clear, concise Problem Statement (3–5 sentences)."
    )
)








OBJECTIVES_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "Task: List high-level objectives of this product.\n"
        "- Keep them crisp and aligned with Angel One’s domain.\n"
        "- Do not include metrics here, only strategic objectives."
    )
)

METRICS_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "taxonomy_context"],
    template=(
        "You are an expert PM at Angel One. Use both domain knowledge and taxonomy to map metrics.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Context:\n{domain_context}\n\n"
        "Taxonomy Context:\n{taxonomy_context}\n\n"
        "Task: Classify metrics into Lead and Lag with their associated L1 (Module) and L2 (Submodule) and give only top 3 lead and lag metrics.\n"
        "Strict Output Format:\n\n"
        "Lead Metrics:\n"
        "1) metric = ... , module = ... , l2 = ...\n"
        "2) ...\n\n"
        "Lag Metrics:\n"
        "1) metric = ... , module = ... , l2 = ...\n"
        "2) ..."
    )
)


FR_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "You are documenting the Functional Requirements.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "List 6–8 functional requirements focusing on end-user and system behavior."
    )
)


US_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "You are writing Agile user stories.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "Write 5–7 user stories in the format:\n"
        "As a [user], I want [goal], so that [benefit]."
    )
)


NFR_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "You are listing Non-Functional Requirements.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "List 5–6 NFRs covering scalability, security, latency, reliability, and compliance."
    )
)


TARGET_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "Identify the target users for this product.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "List 4–6 specific target user groups with justification."
    )
)


RISKS_PROMPT = PromptTemplate(
    input_variables=["title", "description", "compliance_context", "external_context"],
    template=(
        "You are writing Risks and Compliance considerations.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Compliance Knowledge:\n{compliance_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "List 5–6 potential risks, regulatory constraints, and compliance challenges."
    )
)


DEPENDENCIES_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "compliance_context", "external_context"],
    template=(
        "You are writing Dependencies.\n\n"
        "Title: {title}\n"
        "Description: {description}\n\n"
        "Domain Knowledge:\n{domain_context}\n\n"
        "Compliance Knowledge:\n{compliance_context}\n\n"
        "External Research:\n{external_context}\n\n"
        "List key dependencies such as data availability, infra, compliance checks, 3rd-party services."
    )
)


BUSINESS_IMPACT_PLACEHOLDER = "[TO BE FILLED BY BUSINESS TEAM]"






from langchain import PromptTemplate

FR_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "You are the  **Solution Architect** Product Manager/principal Product Manager having more then 20 years of experience in the fintech domain at Angel One(Angel One is one of the leading fintech companies in India , primmarily a stock broker expanding it boundaries in other fintech products ) tasked with documenting the **Functional Requirements (FRs)** of a new fintech product.\n\n"
        " Title: {title}\n"
        " Description: {description}\n\n"
        " Internal Domain Knowledge (authoritative):\n{domain_context}\n\n"
        " External Research (supporting only):\n{external_context}\n\n"
        "---\n"
        " Prioritization of Context:\n"
        "1. Always align requirements with Angel One’s domain knowledge.\n"
        "2. Use external context to validate and extend features where relevant.\n"
        "3. Do not introduce speculative or irrelevant features.\n\n"
        "4. do deep thinking/research to ensure the FRs are comprehensive, specific and aligned with Angel One’s strategic goals.\n\n"
        "5. the FRs should be unambiguous and specific and donot provide general or vague requirements.\n\n"
        " Writing Rules:\n"
        "- Output **6–8 numbered functional requirements**.\n"
        "- Each FR must describe **a specific system or user behavior**.\n"
        "- Keep each FR under *100 words**.\n"
        "- Use clear, testable phrasing.\n"
        "- Exclude non-functional requirements (scalability, latency, compliance) — those go in NFRs.\n"
        "use tabular format to show the requirements  at a glance after listing it out\n"
        "- Exclude design, UI, or technical implementation details.\n\n"
        " Task: Write the final list of functional requirements now."

    )
)
'''


'''
FR_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context"],
    template=(
        "You are a Principal Product Manager with 20+ years of experience in the "
        "fintech domain at Angel One (Angel One is one of the leading fintech companies in India). "
        "Your job is to translate input context into **high-quality, precise, and testable Functional Requirements (FRs)**.\n\n"

        " Product Context\n"
        "Title: {title}\n"
        "Description: {description}\n\n"

        " Authoritative Internal Domain Knowledge (Angel One):\n"
        "{domain_context}\n\n"

        " External Research (supporting only):\n"
        "{external_context}\n\n"


        " Prioritization & Behavior Rules\n"
        "1. All FRs must be explicitly relevant to the **product in the Title & Description**.\n"
        "2. Give **highest weight** to domain_context (internal knowledge).\n"
        "3. Use external_context to enrich with benchmarks, but never override Angel One’s domain.\n"
        "4. If there are conflicting inputs, resolve in favor of **Angel One KB**.\n"
        "5. Avoid duplication: merge overlapping requirements into a single precise FR.\n"
        "6. Do not invent speculative features. Mark unclear ones as 'Clarification Needed'.\n\n"

        " Writing Constraints (must follow exactly)\n"
        "- Output ** numbered FRs**.\n"
        "- Each FR must:\n"
        "   • Be ≤100 words.\n"
        "   • Be **specific, unambiguous, testable**.\n"
        "   • Include 1–2 key acceptance criteria in natural language.\n"
        "   • Include a one-line **Flow** ('Entry → Action → Expected Result').\n"
        "- Exclude non-functional requirements (performance, latency, compliance) — those go in NFRs.\n"
        "- Include UI mockups/visuals — only reference entry points (e.g., 'Explore tab CTA').\n\n"
        "- Include personas relevant to Angel One’s users and product users , majorily it should be the customers of the product.\n"
        "- Add 1–2 acceptance criteria under each story (what must be true for the story to be considered done).\n"
        "- Keep stories concise, actionable, and directly tied to system behavior.\n\n"
        "Do deep thinking/research to ensure the user stories are comprehensive, specific and aligned with Angel One’s strategic goals.\n\n"
        "The user stories should be unambiguous and specific and donot provide general or vague requirements.\n\n"


        " Output Format (strict)\n"
        "1) **4-6 Numbered List of FRs** — Each FR should include:\n"
        "   - Req ID (FR-01, FR-02, ...)\n"
        "   - Functional Requirement\n"
        "   - Acceptance Criteria (1–2 short lines)\n"
        "2) A **Markdown Table** with these columns:\n"
        "| Req ID | Functional Requirement | User Story (short) | Importance | Metrics |\n"
        "|---|---|---|---|---|\n"
        "Populate with FRs above. User Story = best-matched snippet from user_frs. Importance = HIGH/MEDIUM/LOW. "
        "Notes = clarifications, edge cases, dependencies.\n\n"

        " Additional Guidance\n"
        "- Explicitly capture entry points (Explore tab, advisory widget, Watchlist).\n"
        "- For stock lists: specify fields (symbol, qty if in portfolio, LTP, haircut %, Buy CTA, social proof, sorting, filtering).\n"
        "- If a feature is removed/deprecated (e.g., 'Remove Watchlist Tab'), document it as a FR with rationale.\n"
        "- Ensure each FR aligns with at least one **goal/objective** from Angel One KB .\n\n"

        " Task: Now write the final list of Functional Requirements and the Markdown table."
    )
)






CX_PREDICTION_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "external_context", "feedback_context", "taxonomy_context"],
    template=(
        "You are an expert **Customer Success Manager** at Angel One with 20+ years of fintech experience. "
        "Your role is to predict the **Customer Risk Impact** of launching a new product feature by analyzing:\n"
        "- Angel One knowledge (domain_context)\n"
        "- External research (external_context)\n"
        "- Historical customer feedback (feedback_context)\n"
        "- Metrics context (taxonomy_context)\n\n"

        "### Product Context:\n"
        "Title: {title}\n"
        "Description: {description}\n\n"

        "### Angel One Knowledge:\n{domain_context}\n\n"
        "### External Research:\n{external_context}\n\n"
        "### Historical Customer Feedback:\n{feedback_context}\n\n"
        "### Metrics Context:\n{taxonomy_context}\n\n"

        "---\n"
        "### Decision Logic (Strict)\n"
        "1. First, scan taxonomy_context for **'Contact Ratio' under Lag Metrics**:\n"
        "   - If present → Output ONLY:\n\n"
        "| Field            | Value     |\n"
        "|------------------|-----------|\n"
        "| impact_direction | Positive  |\n\n"

        "2. If 'Contact Ratio' is NOT present under Lag Metrics:\n"
        "   - Cross-check all four sources (domain_context, feedback_context, taxonomy_context).\n"
        "   - Weight **historical feedback** - highest  then **Angel One knowledge** and **metrics context** - high, since it captures real customer impact.\n"
        "   - Use domain_context to anchor interpretation, taxonomy_context to map modules/submodules, and external_context for market trends.\n"
        "   - Predict with these rules:\n"
        "     • Impact Level = High / Medium / Low → must align with severity & frequency of similar issues in feedback_context.\n"
        "     • Impact Direction = Stable OR Negative → must align with whether past feedback was neutral vs. harmful.\n"
        "   - Never assign a label unless supported by at least one evidence source.\n"
        "   - If contexts conflict, resolve in favor of **historical feedback**.\n\n"

        "---\n"
        "### Output Format (Strict)\n"
        "- Case 1 (Contact Ratio in Lag Metrics):\n"
        "| Field            | Value     |\n"
        "|------------------|-----------|\n"
        "| impact_direction | Positive  |\n\n"

        "- Case 2 (Contact Ratio not in Lag Metrics):\n"
        "| Field                 | Value                           |\n"
        "|------------------------|---------------------------------|\n"
        "| impact_level           | High / Medium / Low             |\n"
        "| impact_direction       | Stable / Negative               |\n"

        "---\n"
        "### Guidelines:\n"
        "- Always check taxonomy_context first for 'Contact Ratio'.\n"
        "- If it is present then force Positive and nothing else.\n"
        "- If it is absent then use structured reasoning across all contexts.\n"
        "- Drivers must reference **historical feedback evidence** explicitly (e.g., 'Similar rollout in XYZ module led to many complaints').\n"
        "- Cross-validate direction & level: if impact_level = High, then impact_direction cannot be Stable unless feedback_context shows neutral sentiment.\n"
        "- Do not hallucinate. If unsure, use 'Needs clarification'.\n"
        "- Output must always be in **Markdown table format** (never JSON).\n"
    )
)



CX_PREDICTION_PROMPT = PromptTemplate(
    input_variables=["title", "description", "domain_context", "feedback_context", "taxonomy_context", "external_context"],
    template=(
        "You are an expert **Customer Success Manager** at Angel One with 20+ years of fintech experience. "
        "Your task is to predict the **Customer Risk Impact** of a new product feature by analyzing the **pre-evaluated metrics** provided in taxonomy_context.\n\n"

        "### Product Context\n"
        "Title: {title}\n"
        "Description: {description}\n\n"

        "### Angel One Knowledge:\n{domain_context}\n\n"
        "### External Research:\n{external_context}\n\n"
        "### Historical Customer Feedback:\n{feedback_context}\n\n"
        "### Metrics Context (pre-evaluated from METRICS_PROMPT):\n{taxonomy_context}\n\n"

        "---\n"
        "### Decision Logic\n"
        "1. Use the metrics in taxonomy_context as authoritative. **Do NOT reclassify Lead/Lag metrics.**\n"
        "2. If **'Contact Ratio' appears as a Lag Metric**:\n"
        "   - Output a table with only:\n"
        "| Field            | Value     | Justification |\n"
        "|------------------|-----------|---------------|\n"
        "| impact_direction | Positive  |.........|\n\n"
        "3. If **'Contact Ratio' does NOT appear as a Lag Metric**:\n"
        "   - Prioritize evidence from feedback_context > domain_context.\n"
        "   - Predict impact level and direction:\n"
        "     • **Impact Level** = High / Medium / Low (based on severity & frequency in feedback_context)\n"
        "     • **Impact Direction** = Stable / Negative (based on sentiment in feedback_context + domain_context)\n"
        "   - Justifications must cite explicit evidence from feedback_context or domain_context and .\n\n"

        "---\n"
        "### Output Format (Strict Markdown Table)\n"
        "- Case 1 (Contact Ratio in Lag Metrics):\n"
        "| Field            | Value     | Justification |\n"
        "|------------------|-----------|---------------|\n"
        "| impact_direction | Positive  | ...           |\n\n"
        "- Case 2 (Contact Ratio not in Lag Metrics):\n"
        "| Field           | Value               | Justification |\n"
        "|-----------------|---------------------|---------------|\n"
        "| impact_direction| Stable / Negative   | ...           |\n\n"
        "| impact_level    | High / Medium / Low | ...           |\n"


        "---\n"
        "### Guidelines\n"
        "- Do not reclassify metrics; use taxonomy_context as the authoritative source.\n"
        "- Always justify predictions using feedback_context or domain_context evidence.\n"
        "- Output must be in **Markdown table format**, ready for PRD inclusion.\n"
    )
)





CX_PREDICTION_PROMPT = PromptTemplate(
    input_variables=[
        "title",
        "description",
        "domain_context",
        "feedback_context",
        "objectives_context",
        "functional_context",
    ],
    template=(
        "You are an expert **Customer Success Manager** at Angel One with 20+ years of fintech experience. "
        "Act exactly as a senior CSM would: carefully balance customer pain points, business objectives, "
        "and functional details before making a risk prediction.\n\n"

        "### Product Context\n"
        "Title: {title}\n"
        "Description: {description}\n\n"

        "### Inputs for Analysis\n"
        "- Angel One Knowledge:\n{domain_context}\n\n"
        "- Historical Customer Feedback:\n{feedback_context}\n\n"
        "- Product Objectives:\n{objectives_context}\n\n"
        "- User Stories / Functional Requirements:\n{functional_context}\n\n"

        "---\n"
        "### Decision Logic (Human-like Reasoning)\n"
        "1. Map objectives_context + functional_context against historical pain points in feedback_context.\n"
        "   - If strong alignment exists (objectives directly address top complaints) → CX Risk = Positive.\n"
        "   - If partial alignment exists (some complaints addressed, others ignored) → CX Risk = Stable.\n"
        "   - If misalignment or risk of repeating past negative patterns → CX Risk = Negative.\n\n"

        "2. Consider severity & frequency of complaints in feedback_context:\n"
        "   - High severity/frequent → raises impact_level (High).\n"
        "   - Low severity/infrequent → lowers impact_level (Low).\n\n"

        "3. Weigh supporting context:\n"
        "   - Domain_context validates feasibility & alignment with Angel One strategy.\n"

        "4. Always answer like a senior CSM: provide a narrative justification that links evidence → insight → conclusion and use only simple english sentences and strictly donot use any numbers or ids.\n\n"

        "---\n"
        "### Output Format (Strict Markdown Table)\n"
        "| Field            | Value                     | Justification |\n"
        "|------------------|---------------------------|---------------|\n"
        "| impact_direction | Positive / Stable / Negative | Explain clearly why, referencing objectives/functional requirements vs. historical feedback and use only simple english sentences and strictly donot use any numbers or ids . |\n"
        "| impact_level     | High / Medium / Low       | Link to severity & recurrence of feedback issues and whether objectives mitigate them and use only simple english sentences and strictly donot use any numbers or ids. |\n"

        "---\n"
        "### Guidelines\n"
        "- Do NOT hallucinate. Every justification must cite **objectives_context**, **functional_context**, or **feedback_context**.\n"
        "- Write as if explaining to leadership: concise but evidence-driven.\n"
        "- Output must always be in **Markdown table format**, no extra commentary.\n"
    )
)
