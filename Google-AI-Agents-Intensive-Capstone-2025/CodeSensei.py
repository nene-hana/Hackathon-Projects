import streamlit as st
from google import genai

# Load API key safely
API_KEY = st.secrets.get("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)
MODEL_NAME = "models/gemini-2.0-flash"

def review_code(code_block, description):
    prompt = f"""
You are an expert code reviewer.

PULL REQUEST DESCRIPTION:
{description}

CODE TO REVIEW:
{code_block}

TASKS:
1. Identify mistakes, bugs, or bad practices.
2. Suggest improvements.
3. Explain what the code does in simple English.
4. Give a final summary in bullet points.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        # Newer Gemini API returns text directly
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"

st.title("CodeSensei 🧑‍💻 - AI Code Review & Explanation Agent")
st.write("Paste your code and a description to get an automated review + explanation.")

st.subheader("Paste Code Block")
code_input = st.text_area("Code:", height=200, placeholder="Paste code here...")

st.subheader("Description")
pr_description = st.text_area("Describe purpose:", height=80, placeholder="Explain what the code should do...")

if st.button("Review Code"):
    if not code_input.strip() or not pr_description.strip():
        st.error("Please paste both code and description!")
    else:
        st.subheader("Review Output")
        output = review_code(code_input, pr_description)
        st.write(output)
