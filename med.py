
from pywebio.input import input, textarea
from pywebio.output import put_text, put_markdown
from pywebio import start_server
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

# Set your Groq API key
GROQ_API_KEY = "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"

# Initialize the model
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-8b-8192",
    temperature=0.2
)

# Prompt template for medicine recommendation
template = PromptTemplate.from_template("""
You are a helpful and experienced medical assistant. Based on the following patient description, suggest possible medicines (brand/generic names) that are commonly used and safe.

Patient Description:
{input}

Instructions:
- List only 2-3 commonly used medicines with short explanations.
- Include dosage form (tablet, syrup, etc.) if relevant.
- Add precautions if necessary.
""")

def recommend_medicine():
    put_markdown("# ⚕️MEDICO : An AI-based Medicine Recommender 🩺")

    user_input = textarea("Enter Patient Information", placeholder="Example: 42-year-old female with fatigue, weight gain, dry skin, and elevated TSH...", rows=10)

    # Format and send prompt
    formatted_prompt = template.format(input=user_input)
    response = llm.invoke(formatted_prompt)

    put_markdown("### 💊 Recommended Medicines:")
    put_text(response.content)

# Start PyWebIO app
if __name__ == '__main__':
    start_server(recommend_medicine, port=8080, auto_open_webbrowser=True)
