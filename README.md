# 📄 Resume Screening Agent

An AI-powered Resume Screening Agent that evaluates and ranks multiple resumes against a given Job Description (JD), generating an ordered and scored shortlist with clear, transparent reasoning.

The application helps recruiters streamline the initial screening process by automatically extracting relevant candidate information, matching resumes against job requirements, calculating relevance scores and ranking candidates. It also supports exporting the screening results for efficient review and decision-making.


---

## 🚀 Project Overview

Recruiters often need to evaluate many resumes against a single Job Description. Manually comparing skills, experience, and education is time-consuming and inconsistent.

This project automates the initial screening process.

The agent accepts:

* A Job Description
* Multiple resumes in **PDF, DOCX, or TXT** format

It then:

1. Parses the resumes.
2. Extracts candidate information.
3. Identifies skills.
4. Extracts explicitly stated experience.
5. Extracts education information.
6. Compares each resume with the JD using NLP similarity.
7. Calculates a weighted relevance score.
8. Ranks candidates from highest to lowest.
9. Provides reasoning for each candidate's score.
10. Exports the ranked shortlist as CSV and JSON.

The application is designed as a **decision-support tool** and does not replace human review.

---

# 🎯 Agent-Specific Deliverables

This project satisfies the required Resume Screening Agent deliverables.

| Requirement                | Included                     |
| -------------------------- | ---------------------------- |
| Job Description            | ✅ `data/job_description.txt` |
| Sample resume folder       | ✅ `sample_resumes/`          |
| 10+ resumes in one run     | ✅ 12 sample resumes          |
| PDF support                | ✅                            |
| DOCX support               | ✅                            |
| TXT support                | ✅                            |
| NLP similarity             | ✅ TF-IDF + cosine similarity |
| Scored candidate ranking   | ✅                            |
| Ranking reasoning          | ✅                            |
| CSV output                 | ✅                            |
| JSON output                | ✅                            |
| Scoring-method explanation | ✅ `SCORING_METHOD.md`        |
| Runnable UI                | ✅ Streamlit                  |
| Batch execution            | ✅ `run_agent.py`             |

---

# 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Job Description   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Resume Uploads     │
                    │ PDF / DOCX / TXT     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Document Parser    │
                    └──────────┬──────────┘
                               │
                               ▼
             ┌─────────────────────────────────┐
             │ Candidate Information Extraction │
             │                                 │
             │ • Name                          │
             │ • Contact                       │
             │ • Skills                        │
             │ • Experience                    │
             │ • Education                     │
             └────────────────┬────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │    NLP Similarity   │
                    │ TF-IDF + Cosine     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Scoring Engine    │
                    │                     │
                    │ NLP          45%    │
                    │ Skills       35%    │
                    │ Experience   15%    │
                    │ Education     5%    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Candidate Ranking   │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐
       │ Reasoning /      │        │ CSV / JSON       │
       │ Explanation      │        │ Export           │
       └──────────────────┘        └──────────────────┘
```

---

# 🛠️ Tech Stack

### Programming Language

* Python

### Frontend / UI

* Streamlit

### NLP / Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

### Document Processing

* PyPDF
* python-docx

### Data Processing

* Pandas

### Output

* CSV
* JSON

---

# 📁 Project Structure

```text
resume_screening_agent/
│
├── app.py
├── run_agent.py
├── requirements.txt
├── README.md
├── SCORING_METHOD.md
├── PROJECT_MANIFEST.json
├── .gitignore
│
├── core/
│   ├── __init__.py
│   ├── agent.py
│   ├── parsers.py
│   └── scorer.py
│
├── data/
│   └── job_description.txt
│
├── sample_resumes/
│   ├── 01_Aarav_Sharma.txt
│   ├── 02_Meera_Nair.txt
│   ├── 03_Rohan_Patel.docx
│   ├── 04_Sana_Khan.txt
│   ├── 05_Vikram_Rao.txt
│   ├── 06_Isha_Verma.pdf
│   ├── 07_Kabir_Joshi.txt
│   ├── 08_Nisha_Reddy.txt
│   ├── 09_Aditya_Singh.txt
│   ├── 10_Priya_Desai.txt
│   ├── 11_Zoya_Malik.txt
│   └── 12_Arjun_Menon.txt
│
├── output/
│   ├── ranked_candidates.csv
│   └── ranked_candidates.json
│
└── tests/
    └── test_agent.py
```

---

# ⚙️ Setup Instructions

## 1. Clone the repository

```bash
git clone <YOUR_PUBLIC_GITHUB_REPOSITORY_URL>
cd resume_screening_agent
```

Replace `<YOUR_PUBLIC_GITHUB_REPOSITORY_URL>` with the public GitHub repository URL submitted for evaluation.

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

No API key is required.

The application runs locally using open-source Python libraries.

---

# ▶️ Run the Agent

## Option 1 — Streamlit UI

Run:

```bash
streamlit run app.py
```

The Streamlit application will open in the browser.

### Using the UI

### Step 1 — Add Job Description

Either:

* Upload a `.txt`, `.docx`, or `.pdf` Job Description

or

* Paste the Job Description into the text area.

### Step 2 — Upload Resumes

Upload multiple:

* `.pdf`
* `.docx`
* `.txt`

resumes.

The application supports 10+ resumes in a single screening run.

### Step 3 — Start Screening

Click:

```text
🚀 Screen & Rank
```

The agent will parse all resumes and calculate the candidate scores.

### Step 4 — Review Ranking

The UI displays:

* Rank
* Candidate name
* Final score
* NLP relevance
* Skill score
* Experience score
* Education score
* Matched skills
* Missing skills

### Step 5 — Review Reasoning

Each candidate has an expandable explanation showing why the candidate received the calculated score.

### Step 6 — Export

Download:

```text
ranked_candidates.csv
ranked_candidates.json
```

---

# 🖥️ Batch / CLI Execution

The project can also be executed without the Streamlit interface.

The included sample data can be processed with:

```bash
python run_agent.py --jd data/job_description.txt --resumes sample_resumes --output output
```

The command:

1. Reads the Job Description.
2. Reads every supported resume in `sample_resumes/`.
3. Parses candidate information.
4. Calculates relevance scores.
5. Ranks the candidates.
6. Creates CSV and JSON outputs.

Expected output files:

```text
output/
├── ranked_candidates.csv
└── ranked_candidates.json
```

---

# 🧪 Reproduce the Sample Demo

The repository contains:

* 1 sample Job Description
* 12 sample resumes

The sample resumes are explicitly labelled as **synthetic test resumes** and are included only for reproducible testing and demonstration.

Run:

```bash
python run_agent.py --jd data/job_description.txt --resumes sample_resumes --output output
```

This processes all 12 resumes in one run.

The generated files are:

```text
output/ranked_candidates.csv
output/ranked_candidates.json
```

---

# 📊 Scoring Method

The final candidate score is calculated on a scale of **0–100**.

```text
Final Score =
    45% NLP Relevance
  + 35% Skill Match
  + 15% Experience Match
  +  5% Education Match
```

## 1. NLP Relevance — 45%

The Job Description and resume are converted into TF-IDF vectors.

Cosine similarity is then calculated between the two vectors.

This measures the textual relevance between the resume and the Job Description.

---

## 2. Skill Match — 35%

The system identifies technical skills appearing in the Job Description and checks which of those skills are present in the resume.

```text
Skill Score =
Matched JD Skills / Identified JD Skills × 100
```

The skill score contributes 35% to the final score.

---

## 3. Experience Match — 15%

The parser identifies explicitly stated experience such as:

```text
2 years of experience
3+ years of experience
1.5 years of experience
```

If the JD specifies a minimum experience requirement, the candidate's extracted experience is compared against it.

---

## 4. Education Match — 5%

The system checks education-related requirements in the JD against education information extracted from the resume.

---

# 🧠 Why TF-IDF + Cosine Similarity?

TF-IDF with cosine similarity was selected because it provides:

* Local execution
* No API key
* No external service dependency
* Fast processing
* Deterministic results
* Easy reproducibility
* Easy inspection of the scoring pipeline

It is suitable for an intermediate-level technical screening agent while keeping the project lightweight.

---

# 💡 Reasoning / Explainability

The agent does not only return a numerical score.

For each candidate it provides:

* Overall score
* NLP relevance
* Skill coverage
* Matched JD skills
* Missing JD skills
* Experience comparison
* Education match
* Strengths
* Gaps

Example reasoning format:

```text
Overall score: 82.45/100

Strengths:
- Strong NLP relevance
- Strong skill coverage
- Meets the required experience
- Education appears to match

Gaps:
- Missing identified JD skills: Docker
```

The reasoning is generated from information extracted from the resume.

The system does not invent candidate qualifications.

---

# 📤 Output Format

## CSV

The CSV contains fields including:

```text
rank
candidate_name
final_score
nlp_score
skill_score
experience_score
education_score
jd_skills
skills
matched_skills
missing_skills
experience_years
education_summary
reasoning
source_file
```

## JSON

The JSON contains structured candidate records including:

```json
{
  "rank": 1,
  "candidate_name": "...",
  "final_score": 0,
  "nlp_score": 0,
  "skill_score": 0,
  "experience_score": 0,
  "education_score": 0,
  "matched_skills": [],
  "missing_skills": [],
  "reasoning": "..."
}
```

---

# 📸 Sample Inputs and Outputs

## Sample Input

### Job Description

```text
AI / Machine Learning Engineer

Requirements:
- Strong Python and SQL skills.
- Experience with machine learning, NLP and generative AI.
- At least 1 year of relevant experience.
- Bachelor's or master's degree in a related field.
- Experience with REST APIs, Git and Docker is preferred.
```

### Resumes

The `sample_resumes/` folder contains 12 synthetic resumes covering different combinations of:

* Python
* SQL
* Machine Learning
* NLP
* Generative AI
* LLM
* RAG
* Flask
* FastAPI
* Git
* Docker
* Data Analytics
* Backend Development
* Cloud Development

---

## 📤 Output Example

The ranked output follows this structure:

```text
Rank | Candidate | Final Score | NLP Score | Skill Score | Experience | Education
-----|-----------|--------------|-----------|-------------|------------|----------
1    | Candidate A | 82.45      | 76.20     | 91.67       | 100.00     | 100.00
2    | Candidate B | 74.31      | 68.40     | 83.33       | 100.00     | 100.00
3    | Candidate C | 61.72      | 55.10     | 66.67       | 100.00     | 100.00
```

The actual values are generated from the uploaded Job Description and resumes.

---


# 🔍 Handling Missing Information

The system does not fabricate candidate information.

For example, if experience cannot be explicitly extracted from a resume:

```text
Experience: Not explicitly stated
```

If a skill is not detected:

```text
Missing JD skill: <skill>
```

The missing information is not automatically assumed to be present.

---

# ⚖️ Fairness and Responsible Use

This application is intended as a technical screening and decision-support tool.

It should **not** be used as the sole basis for employment decisions.

The scoring system does not intentionally use protected characteristics such as:

* Gender
* Religion
* Race
* Age
* Disability
* Other sensitive personal characteristics

Recruiters should review the original resumes and use human judgment before making hiring decisions.

---

# 🔐 API Keys / Configuration

No API key is required.

The application runs locally using:

```text
Python
Streamlit
Scikit-learn
PyPDF
python-docx
Pandas
```

Therefore there is no `.env` configuration required for the current implementation.

---

# 🧪 Testing

A basic automated test is included in:

```text
tests/test_agent.py
```

Run it with:

```bash
pytest
```

if `pytest` is installed.

The test verifies that:

* Multiple candidates can be screened.
* Candidates are ranked.
* The higher-relevance candidate receives the higher score.
* Ranking starts from 1.

---

# 🔄 Tradeoffs

## Why not use an LLM API?

An LLM API could provide richer semantic understanding and explanations, but it introduces:

* API key requirements
* Cost
* Rate limits
* Network dependency
* Non-deterministic responses

For this submission, a local deterministic pipeline makes the project easier for reviewers to run.

---

## Why not use transformer embeddings?

Transformer embeddings can provide stronger semantic similarity than TF-IDF, especially when two resumes use different terminology for similar concepts.

However, transformer models introduce:

* Larger dependencies
* Model downloads
* Higher memory requirements
* Longer setup time

TF-IDF was chosen to keep the project lightweight and reproducible.

---

## Why use weighted scoring?

A single NLP similarity score would not sufficiently distinguish candidates.

The weighted approach separates:

```text
NLP relevance
Skill match
Experience
Education
```

This also makes the result easier to explain to recruiters.

---

# 🚀 What I Would Improve With More Time

With additional development time, I would add:

1. Transformer-based sentence embeddings for stronger semantic matching.
2. Better extraction of years of experience from employment date ranges.
3. Required vs preferred skill weighting.
4. Experience and education requirement parsing with more robust NLP.
5. OCR support for scanned/image-based PDFs.
6. Candidate comparison charts and analytics.
7. Configurable scoring weights through the UI.
8. Human-review workflow for shortlisted candidates.
9. Bias and fairness evaluation before production use.
10. Optional embedding-based ranking as an alternative to TF-IDF.

---

# 📌 Limitations

The current implementation has several deliberate limitations:

* TF-IDF measures lexical similarity rather than deep semantic similarity.
* Skill extraction uses a technical skill vocabulary.
* Experience extraction depends on explicitly stated experience text.
* Scanned PDFs without an extractable text layer may require OCR.
* Education extraction is keyword-based.
* The ranking should be treated as an initial shortlist rather than a final hiring decision.

