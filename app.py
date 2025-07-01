import streamlit as st
from logic import run_simulation
from personas import get_persona
from utils import export_to_pdf, generate_life_advice

st.set_page_config(page_title="LifeSim", layout="wide")
st.title("🧬 LifeSim: Simulate Your Future Path")

st.markdown("Simulate your life journey over 5 years based on your choices, lifestyle, and mindset.")

# === Input Form ===
with st.form("lifesim_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.header("🎭 Scenario A")
        persona_a = st.selectbox("Persona", ["The Dreamer", "The Hustler", "The Balanced One"], key="persona_a")
        career_a = st.selectbox("Career Path", ["engineer", "founder", "freelancer"], key="career_a")
        lifestyle_a = st.selectbox("Lifestyle", ["balanced", "burnout", "chilled"], key="lifestyle_a")
        habit_a = st.selectbox("Financial Habit", ["spender", "saver", "investor"], key="habit_a")
        relationship_a = st.selectbox("Relationship Status", ["single", "in a relationship", "breakup"], key="rel_a")

    with col2:
        st.header("🧪 Scenario B (Optional)")
        enable_b = st.checkbox("Compare with a second scenario?", value=False)

        if enable_b:
            persona_b = st.selectbox("Persona", ["The Dreamer", "The Hustler", "The Balanced One"], key="persona_b")
            career_b = st.selectbox("Career Path", ["engineer", "founder", "freelancer"], key="career_b")
            lifestyle_b = st.selectbox("Lifestyle", ["balanced", "burnout", "chilled"], key="lifestyle_b")
            habit_b = st.selectbox("Financial Habit", ["spender", "saver", "investor"], key="habit_b")
            relationship_b = st.selectbox("Relationship Status", ["single", "in a relationship", "breakup"], key="rel_b")

    submitted = st.form_submit_button("Simulate My Life")

# === Run Simulations ===
if submitted:
    user_a = {
        "career": career_a,
        "lifestyle": lifestyle_a,
        "habits": habit_a,
        "relationship": relationship_a,
        "persona": get_persona(persona_a)
    }

    report_a, h1, s1, c1, m1 = run_simulation(user_a)

    st.subheader("📋 Life Report: Scenario A")
    st.text_area("Simulation Result (A)", report_a, height=400)

    st.line_chart({
        "Happiness (A)": h1,
        "Stress (A)": s1,
        "Career Growth (A)": c1,
    })

    # PDF Export
    if st.button("📝 Download Scenario A as PDF"):
        filename = export_to_pdf(report_a)
        with open(filename, "rb") as f:
            st.download_button("Download PDF", data=f, file_name=filename, mime="application/pdf")

    # AI Life Advice
    if st.button("🤖 Get AI Life Advice (A)"):
        advice = generate_life_advice(report_a)
        st.success(f"💡 {advice}")

    # === If Comparing ===
    if enable_b:
        user_b = {
            "career": career_b,
            "lifestyle": lifestyle_b,
            "habits": habit_b,
            "relationship": relationship_b,
            "persona": get_persona(persona_b)
        }

        report_b, h2, s2, c2, m2 = run_simulation(user_b)

        st.subheader("📋 Life Report: Scenario B")
        st.text_area("Simulation Result (B)", report_b, height=400)

        st.line_chart({
            "Happiness (B)": h2,
            "Stress (B)": s2,
            "Career Growth (B)": c2,
        })

        if st.button("📝 Download Scenario B as PDF"):
            filename = export_to_pdf(report_b, filename="LifeSim_Report_B.pdf")
            with open(filename, "rb") as f:
                st.download_button("Download PDF (B)", data=f, file_name=filename, mime="application/pdf")

        if st.button("🤖 Get AI Life Advice (B)"):
            advice_b = generate_life_advice(report_b)
            st.success(f"💡 {advice_b}")
