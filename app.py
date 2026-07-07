import streamlit as st

from utils.parser import extract_pdf_text
from utils.parser import extract_docx_text

from src.predict import predict_role

st.set_page_config(
    page_title="TalentLens AI",
    page_icon="📄",
    layout="wide"
)

st.title("TalentLens AI")

st.write("AI Resume Screening & Job Role Prediction")

uploaded = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded:

    if uploaded.name.endswith(".pdf"):

        resume = extract_pdf_text(uploaded)

    else:

        resume = extract_docx_text(uploaded)

    role = predict_role(resume)

    st.success(f"Predicted Role: {role}")