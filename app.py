import streamlit as st

from utils.parser import extract_pdf_text
from utils.parser import extract_docx_text

from src.predict import predict_role
from src.ats import calculate_resume_score
from src.recommendations import get_recommendations

st.set_page_config(
    page_title="TalentLens AI",
    page_icon="📄",
    layout="wide"
)

st.title("🚀 TalentLens AI")

st.caption("AI Resume Screening & Skill Recommendation Platform")

uploaded = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
)

if uploaded:

    if uploaded.name.endswith(".pdf"):
        resume = extract_pdf_text(uploaded)
    else:
        resume = extract_docx_text(uploaded)

    role = predict_role(resume)

    score, found, missing = calculate_resume_score(
        resume,
        role
    )

    courses = get_recommendations(role)

    col1,col2 = st.columns(2)

    with col1:

        st.success("Predicted Role")

        st.subheader(role)

        st.metric(
            "ATS Resume Score",
            f"{score}/100"
        )

    with col2:

        st.info("Resume Statistics")

        st.write("Characters :",len(resume))

        st.write("Words :",len(resume.split()))

    st.divider()

    st.subheader("✅ Skills Found")

    if found:

        for skill in found:

            st.success(skill)

    else:

        st.warning("No matching skills found")

    st.divider()

    st.subheader("❌ Missing Skills")

    if missing:

        for skill in missing:

            st.error(skill)

    else:

        st.success("Excellent!")

    st.divider()

    st.subheader("📚 Learning Recommendations")

    for course in courses:

        st.write("📘",course)