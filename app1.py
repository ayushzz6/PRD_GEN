import streamlit as st
from orchestrator import PRDGenerator
from utils import logging
from deep_research import run_deep_research

st.set_page_config(page_title="PRD Generator", layout="wide")

st.title(" Angel One – PRD Generator")
st.markdown(
    """
This tool generates a structured **Product Requirements Document (PRD)**.  
"""
)

# Sidebar config
st.sidebar.header("Configuration")
llm_model = st.sidebar.text_input("PRD Model", value="gpt-4.1")
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.2, 0.05)
use_research = st.sidebar.checkbox("Enable Deep Research (O3/O4)", value=True)
research_model = st.sidebar.text_input("Deep Research Model", value="o3")

# Form for input
with st.form("prd_form"):
    st.subheader(" Enter Product Details")
    title = st.text_input("PRD Title", placeholder="e.g. Smart Trade Signal Generator")
    description = st.text_area(
        "Product Description (100–200 words)",
        height=200,
        placeholder="Describe the product in detail...",
    )
    submitted = st.form_submit_button("Generate PRD")

if submitted:
    if not title.strip() or not description.strip():
        st.error(" Please enter both Title and Description.")
    else:
        #  Optional Deep Research
        if use_research:
            with st.spinner(" Running Deep Research..."):
                try:
                    research_path = run_deep_research(title, description, model=research_model)
                    st.success(f"Deep Research completed. Saved at {research_path}")
                except Exception as e:
                    st.error(" Deep Research failed. Check logs.")
                    logging.exception("Deep Research error")
                    st.stop()
        else:
            st.info(" Deep Research skipped. Using only Domain, Taxonomy, Feedback and Compliance KBs.")

        # Generate PRD
        with st.spinner("Generating PRD..."):
            try:
                prd = PRDGenerator(llm_model=llm_model, temp=temperature)
                result = prd.generate(title=title, description=description)
                st.success(" PRD Generated Successfully!")

                # Tabs for results
                tabs = st.tabs(
                    [
                        " Full PRD",
                        " Problem",
                        " Goals & Objectives",
                        " Lead & Lag Metrics",
                        " Target Users",
                        " Competitors",
                        " Functional Requirements and User Stories",
                        " CX Predictions",
                        " Risks & Dependencies",
                    ]
                )

                with tabs[0]:
                    st.download_button(
                        " Download PRD (Markdown)",
                        data=result["markdown"],
                        file_name=f"{title.replace(' ', '_')}.md",
                        mime="text/markdown",
                    )
                    st.markdown(result["markdown"])

                with tabs[1]:
                    st.markdown(result["problem"])
                with tabs[2]:
                    st.markdown(result["objectives"])
                with tabs[3]:
                    st.markdown(result["metrics"])
                with tabs[4]:
                    st.markdown(result["targets"])
                with tabs[5]:
                    st.markdown(result["competitors"])
                with tabs[6]:
                    st.markdown(result["frs"])
                with tabs[7]:
                    st.markdown(result["cx"])
                with tabs[8]:
                    st.markdown(result["risks"])


            except Exception as e:
                st.error("Failed to generate PRD. Check logs.")
                logging.exception("Streamlit PRD generation error")


