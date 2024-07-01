import streamlit as st
import PyPDF2
from docx import Document
import requests
import pandas as pd
from io import BytesIO

# Groq LLaMA-3 API key (set your API key here)
GROQ_API_KEY = 'your_groq_llama3_api_key'
GROQ_API_URL = 'https://api.groq.ai/llama3/generate'  # Update with the actual API URL if different

# Function to generate summary using Groq LLaMA-3
def generate_summary(text):
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': f"Summarize the following text:\n\n{text}",
        'max_tokens': 150,
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    response.raise_for_status()
    summary = response.json()['choices'][0]['text'].strip()
    return summary

# Function to process PDF files
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages
    text = ""
    for page in range(num_pages):
        text += pdf_reader.getPage(page).extractText()
    return text

# Function to process DOCX files
def read_docx(file):
    doc = Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []

def show():
    st.title("Dialogue Summarization")

    # File uploader for PDF and DOCX
    uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

    # Text area for plain text input
    input_text = st.text_area("Or enter text directly")

    # Summarize button
    if st.button("Summarize"):
        if uploaded_file:
            if uploaded_file.type == "application/pdf":
                input_text = read_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                input_text = read_docx(uploaded_file)

        if input_text:
            summary = generate_summary(input_text)
            st.session_state.history.append({"input": input_text, "summary": summary, "feedback": None})
            st.success("Summary generated!")
        else:
            st.error("Please provide text or upload a file.")

    # Display chat history
    if st.session_state.history:
        for chat in reversed(st.session_state.history):
            st.write(f"**Input:** {chat['input']}")
            st.write(f"**Summary:** {chat['summary']}")
            if chat["feedback"] is None:
                feedback = st.radio(f"Rate the summary for the above input:", ["Good", "Average", "Poor"], key=f"feedback_{len(st.session_state.history)}")
                if feedback:
                    chat["feedback"] = feedback
            else:
                st.write(f"**Feedback:** {chat['feedback']}")

    # Save chat history as CSV
    if st.button("Save History"):
        df = pd.DataFrame(st.session_state.history)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Chat History",
            data=csv,
            file_name="chat_history.csv",
            mime="text/csv"
        )
