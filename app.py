import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="Industrial Brain AI",
    page_icon="🏭"
)

st.title("🏭 Industrial Brain AI")
st.subheader("Unified Asset & Operations Brain")

uploaded_file = st.file_uploader(
    "Upload Industrial Document",
    type=["pdf"]
)

document_text = ""

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    for page in pdf.pages:
        text = page.extract_text()
        if text:
            document_text += text

    st.success("Document processed successfully!")

    st.write("Characters Loaded:", len(document_text))

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("Get Answer"):

        with st.spinner("Analyzing..."):

            prompt = f"""
            You are an industrial knowledge assistant.

            Document:
            {document_text[:30000]}

            Question:
            {question}

            Give a detailed answer.
            Mention the relevant document section if possible.
            """

            response = model.generate_content(prompt)

            st.subheader("Answer")
            st.write(response.text)

# Maintenance Intelligence

st.divider()

st.subheader("Maintenance Intelligence Agent")

issue = st.text_area(
    "Describe Equipment Issue"
)

if st.button("Generate Recommendation"):

    prompt = f"""
    You are a senior maintenance engineer.

    Problem:
    {issue}

    Provide:

    1. Possible Causes
    2. Recommended Inspection
    3. Corrective Action
    4. Risk Level
    """

    response = model.generate_content(prompt)

    st.write(response.text)

# Entity Extraction

st.divider()

st.subheader("Equipment Entity Extraction")

sample = st.text_area(
    "Paste Maintenance Report"
)

if st.button("Extract Equipment Tags"):

    import re

    tags = re.findall(
        r"[A-Z]{1,5}-\d+",
        sample
    )

    st.write("Detected Equipment Tags:")
    st.write(tags)

# Dashboard

st.divider()

st.subheader("System Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("AI Engine", "Gemini")
col2.metric("Status", "Online")
col3.metric("Mode", "Industrial")