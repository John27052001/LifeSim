import openai
from fpdf import FPDF 
import os
# === 📝 Generate a PDF Report ===
def export_to_pdf(report_text, filename="LifeSim_Report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in report_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename

# === 🤖 Generate AI Life Advice ===
def generate_life_advice(simulation_text):
    openai.api_key = "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" 

    prompt = (
        "Based on this simulated life path, provide a short piece of advice "
        "as if you're a wise life coach. Keep it kind, insightful, and no more than 2 sentences.\n\n"
        f"Life Summary:\n{simulation_text[-700:]}"  # last 700 chars
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use gpt-4 if available
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60,
            temperature=0.7,
        )
        advice = response['choices'][0]['message']['content'].strip()
        return advice
    except Exception as e:
        return f"⚠️ AI advice not available: {e}"
