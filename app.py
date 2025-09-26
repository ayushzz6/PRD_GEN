import streamlit as st
from orchestrator import PRDGenerator
from utils import logging
from deep_research import run_deep_research
from dotenv import load_dotenv
import os
import time


load_dotenv()

st.set_page_config(page_title="PRD Generator", layout="wide")
st.title("Angel One – PRD Generator")
st.markdown("This tool generates a structured **Product Requirements Document (PRD)**.")

# Sidebar configuration
st.sidebar.header("Configuration")
llm_model = st.sidebar.text_input("PRD Model", value="gpt-5")
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.15, 0.05)
use_research = st.sidebar.checkbox("Enable Deep Research (O3/O4)", value=True)
research_model = st.sidebar.text_input("Deep Research Model", value="o3")

# Input form
with st.form("prd_form"):
    st.subheader("Enter Product Details")
    title = st.text_input("PRD Title", placeholder="e.g. Smart Trade Signal Generator")
    description = st.text_area(
        "Product Description (100–200 words)",
        height=200,
        placeholder="Describe the product in detail..."
    )
    submitted = st.form_submit_button("Generate PRD")

if submitted:
    if not title.strip() or not description.strip():
        st.error("Please enter both Title and Description.")
        st.stop()

    progress_text = st.empty()

    # Optional Deep Research
    if use_research:
        progress_text.text("Running Deep Research...")
        try:
            research_path = run_deep_research(title, description, model=research_model)
            progress_text.text(f"Deep Research completed. Saved at {research_path}")
        except Exception as e:
            st.error(f"Deep Research failed: {str(e)}")
            logging.exception("Deep Research error")
            st.stop()
    else:
        progress_text.text("Deep Research skipped. Using only internal KBs.")

    # Generate PRD
    try:
        prd_generator = PRDGenerator(llm_model=llm_model, temp=temperature)

        progress_text.text("Generating full PRD... This may take a few minutes.")
        start_time = time.time()
        result = prd_generator.generate(title=title, description=description)
        end_time = time.time()

        progress_text.text(f"PRD Generated Successfully! (Time taken: {int(end_time - start_time)}s)")

        # Tabs for sections
        tabs = st.tabs([
            "Full PRD", "Problem", "Objectives", "Metrics",
            "Target Users", "Competitors", "FR & User Stories",
            "CX Predictions", "Risks"
        ])

        # Full PRD tab
        with tabs[0]:
            st.download_button(
                "Download PRD (Markdown)",
                data=result["markdown"],
                file_name=f"{title.replace(' ', '_')}.md",
                mime="text/markdown"
            )
            st.markdown(result["markdown"])

        # Section-wise tabs
        with tabs[1]: st.markdown(result["problem"])
        with tabs[2]: st.markdown(result["objectives"])
        with tabs[3]: st.markdown(result["metrics"])
        with tabs[4]: st.markdown(result["targets"])
        with tabs[5]: st.markdown(result["competitors"])
        with tabs[6]: st.markdown(result["frs"])
        with tabs[7]: st.markdown(result["cx"])
        with tabs[8]: st.markdown(result["risks"])

    except Exception as e:
        st.error(f"Failed to generate PRD: {str(e)}")
        logging.exception("Streamlit PRD generation error")
        st.stop()
