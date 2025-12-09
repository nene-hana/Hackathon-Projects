# CodeSensei 🧑‍💻  
### AI‑Powered Code Review & Explanation Tool (Streamlit + Gemini)

---

## 📌 Overview

CodeSensei is an AI‑powered application designed to review code, detect mistakes, provide improvement suggestions, and generate simple explanations of how the code works.  
This tool leverages **Google Gemini 2.0 Flash** and a clean **Streamlit-based UI**, making it ideal for students, developers, and hackathon participants who want fast, intelligent code insights.

---

## 🎯 Features

- 🔍 **Automated Code Review** — Detects errors, bad practices, and potential bugs.  
- 🚀 **Improvement Suggestions** — Offers optimized ways to structure or clean code.  
- 📘 **Beginner-Friendly Explanations** — Converts technical code into simple English.  
- 📄 **Pull Request‑style Summary** — Provides a final bullet-point overview.  
- 🌐 **Web‑based UI** using Streamlit for easy interactions.  
- 🔑 **Secure API Key Handling** using Streamlit Secrets.  

---

## 🧠 Technology Stack

- **Python 3.10+**  
- **Streamlit** — UI Framework  
- **Google Generative AI (Gemini API)** — LLM Backend  
- **Gemini 2.0 Flash Model**  
- **Prompt‑driven Code Analysis**  

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository  
```bash
git clone <your-repo-link>
cd project
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App  
```bash
streamlit run CodeSensei.py
```

---

## 🧩 CodeSensei — Source Code

```python
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
```

---

## 📦 Requirements

```
streamlit
google-generativeai
```

---
## 📌 Sample Usage

Below is an example demonstrating how to use **CodeSensei — AI Code Review & Explanation Agent** inside the Streamlit interface.

### 🔹 Step 1: Run the Application
To start CodeSensei, execute:

```bash
streamlit run CodeSensei.py
```

### 🔹 Step 2: Enter Code to Review
Paste any Python code into the **“Code”** text area.  
**Example code:**

```python
numbers = [1, 2, 3, 4, 5]

total = 0
for n in numbers:
    total += n

print("Sum:", total)
```

### 🔹 Step 3: Provide a Description
In the **“Describe purpose”** field, enter a short explanation such as:

```
This code calculates the sum of a list of numbers using a for‑loop.
```

### 🔹 Step 4: Click “Review Code”
CodeSensei will automatically:

- Analyze the code  
- Identify mistakes or inefficiencies  
- Suggest improvements  
- Explain the code in simple English  
- Provide a neat bullet‑point summary  

### 🔹 Example Output
The AI may return something like:

```
This loop correctly calculates the sum of the numbers, but it can be simplified using Python’s built-in sum() function.

Explanation:
- A list named "numbers" is created.
- A variable "total" is initialized to zero.
- Each value in the list is added to "total".
- Finally, the sum is printed.

Suggestions:
- Replace the manual loop with: total = sum(numbers)
```
---

## 🏆 Why CodeSensei?

- Made specifically for hackathon‑friendly demos  
- Extremely lightweight  
- Clean UI  
- Uses state‑of‑the‑art Gemini models  
- Perfect for debugging, learning, code reviewing, and teaching  

---

## 🙌 Team

Built by:  
**TEAM PRIMA QUESTA** in accordance with **GOOGLE AI AGENTS INTENSIVE COURSE 2025** hackathon Capstone

---

## 📄 License

This project is for educational and hackathon use.

---

