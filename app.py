import json,pandas as pd,streamlit as st 
from core.agent import ResumeScreeningAgent 
from core.parsers import parse_resume_file,parse_text_file 
 
st.set_page_config(
    page_title="Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)

# =========================
# CUSTOM UI / CSS
# =========================
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #64748b;
        margin-bottom: 30px;
    }

    /* Section cards */
    .section-card {
        background: white;
        padding: 22px 25px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.06);
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 5px;
    }

    .section-description {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 15px;
    }

    /* Metric cards */
    .metric-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
        text-align: center;
    }

    .metric-number {
        font-size: 28px;
        font-weight: 800;
        color: #4f46e5;
    }

    .metric-label {
        font-size: 13px;
        color: #64748b;
        margin-top: 3px;
    }

    /* Primary button */
    .stButton > button {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.25);
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: #f8fafc;
        border-radius: 12px;
    }

    /* Text area */
    textarea {
        border-radius: 10px !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #eef2ff 0%, #f8fafc 100%);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #1e293b;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    /* Expanders */
    .streamlit-expanderHeader {
        background: white;
        border-radius: 10px;
        font-weight: 600;
    }

    /* Success message */
    .success-card {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #065f46;
        padding: 14px 18px;
        border-radius: 10px;
        margin: 15px 0;
        font-weight: 600;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">📄 Resume Screening Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered resume screening • Extract → Score → Rank → Explain → Export</div>',
    unsafe_allow_html=True
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.header("⚙️ Scoring Weights")

    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">45%</div>
        <div class="metric-label">NLP Relevance</div>
    </div>
    <br>
    <div class="metric-card">
        <div class="metric-number">35%</div>
        <div class="metric-label">Skill Match</div>
    </div>
    <br>
    <div class="metric-card">
        <div class="metric-number">15%</div>
        <div class="metric-label">Experience</div>
    </div>
    <br>
    <div class="metric-card">
        <div class="metric-number">5%</div>
        <div class="metric-label">Education</div>
    </div>
    """, unsafe_allow_html=True)

    st.info("🔒 No API key required. Processing is local.")


# =========================
# JOB DESCRIPTION
# =========================

st.markdown("""
<div class="section-card">
    <div class="section-title">1️⃣ Job Description</div>
    <div class="section-description">
        Upload a job description or paste it manually.
    </div>
</div>
""", unsafe_allow_html=True)

jd_file = st.file_uploader(
    "Upload JD",
    type=["txt", "docx", "pdf"]
)

jd = st.text_area(
    "Or paste the JD",
    height=220,
    placeholder="Paste the job description here..."
)

if jd_file:
    try:
        jd = parse_text_file(jd_file.name, jd_file.getvalue())
        st.success("✅ JD loaded successfully.")
    except Exception as e:
        st.error(str(e))


# =========================
# RESUMES
# =========================

st.markdown("""
<div class="section-card">
    <div class="section-title">2️⃣ Candidate Resumes</div>
    <div class="section-description">
        Upload multiple resumes in PDF, DOCX, or TXT format.
    </div>
</div>
""", unsafe_allow_html=True)

files = st.file_uploader(
    "Upload 10+ resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if files:
    st.markdown(
        f"""
        <div class="success-card">
            📁 {len(files)} resume(s) selected and ready for screening.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# SCREENING
# =========================

if st.button(
    "🚀 Screen & Rank Candidates",
    type="primary",
    use_container_width=True
):

    if not jd.strip():
        st.error("⚠️ Provide a Job Description.")
        st.stop()

    if not files:
        st.error("⚠️ Upload at least one resume.")
        st.stop()

    candidates = []
    errors = []

    for f in files:
        try:
            candidates.append(
                parse_resume_file(f.name, f.getvalue())
            )
        except Exception as e:
            errors.append(f"{f.name}: {e}")

    for e in errors:
        st.warning(e)

    results = ResumeScreeningAgent().screen(jd, candidates)

    df = pd.DataFrame(results)

    st.success(f"✅ Successfully screened {len(results)} resume(s).")


    # =========================
    # SUMMARY CARDS
    # =========================

    st.subheader("📊 Screening Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{len(results)}</div>
                <div class="metric-label">Candidates Screened</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        avg_score = df["final_score"].mean()

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{avg_score:.1f}</div>
                <div class="metric-label">Average Score</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        top_score = df["final_score"].max()

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{top_score:.1f}</div>
                <div class="metric-label">Top Candidate Score</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =========================
    # RANKED SHORTLIST
    # =========================

    st.subheader("🏆 Ranked Shortlist")

    cols = [
        "rank",
        "candidate_name",
        "final_score",
        "nlp_score",
        "skill_score",
        "experience_score",
        "education_score",
        "matched_skills",
        "missing_skills",
        "experience_years_display"
    ]

    show = df[cols].copy()

    for c in ["matched_skills", "missing_skills"]:
        show[c] = show[c].apply(
            lambda x: ", ".join(x)
        )

    st.dataframe(
        show,
        use_container_width=True,
        hide_index=True,
        column_config={
            "final_score": st.column_config.ProgressColumn(
                "Final Score",
                min_value=0,
                max_value=100,
                format="%.2f"
            ),
            "nlp_score": st.column_config.NumberColumn(
                "NLP",
                format="%.2f"
            ),
            "skill_score": st.column_config.NumberColumn(
                "Skills",
                format="%.2f"
            ),
            "experience_score": st.column_config.NumberColumn(
                "Experience",
                format="%.2f"
            ),
            "education_score": st.column_config.NumberColumn(
                "Education",
                format="%.2f"
            )
        }
    )


    # =========================
    # REASONING
    # =========================

    st.subheader("🧠 Candidate Reasoning")

    for r in results:

        with st.expander(
            f"#{r['rank']} — {r['candidate_name']} — "
            f"{r['final_score']:.2f}/100"
        ):

            st.markdown(r["reasoning"])

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Matched Skills")
                st.write(
                    ", ".join(r["matched_skills"]) or "None"
                )

            with col2:
                st.markdown("### ❌ Missing Skills")
                st.write(
                    ", ".join(r["missing_skills"]) or "None"
                )

            st.markdown("### 🛠️ Extracted Skills")
            st.write(
                ", ".join(r["skills"]) or "None"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🎓 Education")
                st.write(
                    r["education_summary"]
                    or "Not explicitly extracted"
                )

            with col2:
                st.markdown("### 💼 Experience")
                st.write(
                    r["experience_years_display"]
                )


    # =========================
    # EXPORT
    # =========================

    st.subheader("📥 Export Results")

    c1, c2 = st.columns(2)

    csv = df.copy()

    for c in [
        "jd_skills",
        "skills",
        "matched_skills",
        "missing_skills"
    ]:
        csv[c] = csv[c].apply(
            lambda x: ", ".join(x)
        )

    with c1:
        st.download_button(
            "⬇️ Download Ranked CSV",
            csv.to_csv(index=False).encode(),
            "ranked_candidates.csv",
            "text/csv",
            use_container_width=True
        )

    with c2:
        st.download_button(
            "⬇️ Download Ranked JSON",
            json.dumps(
                results,
                indent=2
            ).encode(),
            "ranked_candidates.json",
            "application/json",
            use_container_width=True
        )


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div class="footer">
        📄 Resume Screening Agent • Local NLP Processing •
        Extract → Score → Rank → Explain → Export
    </div>
    """,
    unsafe_allow_html=True
)