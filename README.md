# 📄 Resume Screening Agent

An NLP-powered Resume Screening Agent that ranks multiple resumes against a given Job Description (JD) and produces an ordered, scored shortlist with transparent reasoning.

The application is designed to help recruiters quickly screen a batch of candidates by automatically extracting relevant information from resumes, comparing candidates with the job requirements, calculating relevance scores, ranking candidates, and exporting the results.

---

## 🚀 Project Overview

Recruiters often need to review a large number of resumes for a single job opening. Manually comparing every resume with a Job Description can be time-consuming and inconsistent.

The **Resume Screening Agent** automates the initial screening process.

It accepts:

* A Job Description
* Multiple resumes in PDF, DOCX, or TXT format

It then:

1. Parses the uploaded resumes.
2. Extracts candidate information.
3. Identifies skills, experience, and education.
4. Compares resume content with the Job Description using NLP.
5. Calculates a relevance score.
6. Ranks all candidates.
7. Provides reasoning for every candidate's score.
8. Exports the final shortlist as CSV or JSON.

The system can process **10+ resumes in a single run**.

---

## ✨ Key Features

### 📑 Resume Parsing

Supports:

* PDF
* DOCX
* TXT

The parser extracts available information such as:

* Candidate name
* Email
* Skills
* Years of experience
* Education
* Education
* Missing skills

Missing information is not fabricated. If a value cannot be extracted, the system reports it as unavailable.

---

### 📝 Job Description Processing

The application accepts a Job Description through:

* Text input
* TXT file
* DOCX file
* PDF file

The JD is analyzed to identify relevant technical skills, experience requirements, and education requirements.

---

### 🧠 NLP-Based Relevance Scoring

The project uses **TF-IDF vectorization and cosine similarity** to measure the textual relevance between the Job Description and each resume.

This allows the system to compare the overall terminology and content of a candidate's resume with the requirements of the position.

---

## 📊 Scoring Methodology

Each candidate receives a final score between **0 and 100**.

The score is calculated using four components:

| Component        | Weight |
| ---------------- | -----: |
| NLP Relevance    |    45% |
| Skill Match      |    35% |
| Experience Match |    15% |
| Education Match  |     5% |

### Final Score

```text
Final Score =
    0.45 × NLP Relevance
  + 0.35 × Skill Match
  + 0.15 × Experience Match
  + 0.05 × Education Match
```

### 1. NLP Relevance — 45%

TF-IDF is applied to the Job Description and resume text.

Cosine similarity is then used to determine how closely the resume content matches the JD.

### 2. Skill Match — 35%

Technical skills identified in the Job Description are compared with skills identified in the resume.

```text
Skill Score =
Matched JD Skills / Identified JD Skills × 100
```

The system also reports:

* Matched skills
* Missing skills

### 3. Experience Match — 15%

The system extracts explicit experience information such as:

```text
3 years of experience
2.5 years of experience
5+ years of experience
```

If the Job Description contains a minimum experience requirement, the candidate's extracted experience is compared against it.

### 4. Education Match — 5%

The system checks whether the education level or degree requested by the Job Description appears in the candidate's resume.

---

## 🏆 Candidate Ranking

After calculating the scores, candidates are sorted in descending order.

The output contains:

```text
Rank
Candidate Name
Final Score
NLP Score
Skill Score
Experience Score
Education Score
Matched Skills
Missing Skills
Experience
Education
Reasoning
```

The ranking is deterministic and uses additional score components as tie-breakers.

---

## 💡 Explainable Screening

The system does not return only a numerical score.

For every candidate, it provides reasoning such as:

* Strong or moderate NLP relevance
* Skill coverage
* Whether the experience requirement is met
* Education match
* Missing Job Description skills

This makes the shortlist easier to inspect and understand.

---

## 🖥️ User Interface

The project uses **Streamlit** to provide a simple recruiter-friendly interface.

### Workflow

```text
Job Description
      ↓
Upload Resumes
      ↓
Resume Parsing
      ↓
Information Extraction
      ↓
NLP Similarity
      ↓
Skill Matching
      ↓
Experience Matching
      ↓
Education Matching
      ↓
Final Score
      ↓
Candidate Ranking
      ↓
Reasoning
      ↓
CSV / JSON Export
```

---

## 📂 Project Structure

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
│   ├── README.md
│   ├── 01_Aarav_Sharma.txt
│   ├── 02_Meera_Nair.txt
│   ├── ...
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

## 🛠️ Technologies Used

### Programming Language

* Python

### Frontend / UI

* Streamlit

### NLP / Machine Learning

* Scikit-learn
* TF-IDF
* Cosine Similarity

### Document Processing

* PyPDF
* python-docx

### Data Processing

* Pandas

### Output Formats

* CSV
* JSON

### Development Tools

* VS Code
* Git
* GitHub

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd resume_screening_agent
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Run the Batch Version

The project also includes a command-line runner.

```bash
python run_agent.py \
    --jd data/job_description.txt \
    --resumes sample_resumes \
    --output output
```

The generated files are:

```text
output/ranked_candidates.csv
output/ranked_candidates.json
```

---

## 📥 Using the Web Application

### Step 1 — Add Job Description

Paste the JD into the text area or upload a:

* PDF
* DOCX
* TXT

### Step 2 — Upload Resumes

Upload multiple resumes simultaneously.

The application supports:

```text
PDF
DOCX
TXT
```

For the challenge requirement, upload **10 or more resumes** in a single run.

### Step 3 — Start Screening

Click:

```text
🚀 Screen & Rank
```

The system processes all readable resumes.

### Step 4 — Review Ranking

The application displays an ordered shortlist containing each candidate's score and extracted information.

### Step 5 — Review Reasoning

Expand an individual candidate to view:

* Score explanation
* Matched skills
* Missing skills
* Extracted experience
* Education information

### Step 6 — Export Results

Download:

```text
ranked_candidates.csv
```

or

```text
ranked_candidates.json
```

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

## 🧪 Sample Data

The repository contains a sample Job Description and **12 synthetic test resumes**.

These files are included only to demonstrate the required 10+ resume batch-processing capability.

For actual recruitment screening, replace the sample files with real resumes.

---

## 🔍 Testing

The project includes automated tests for the screening engine.

Run:

```bash
pytest tests/
```

The tests verify the ranking pipeline and scoring behavior.

---

## 📄 Scoring Documentation

A separate explanation of the scoring methodology is available in:

```text
SCORING_METHOD.md
```

This document explains:

* NLP scoring
* Skill matching
* Experience scoring
* Education scoring
* Final score calculation
* Ranking logic
* Limitations

## 👩‍💻 Purpose

This project demonstrates how Natural Language Processing can be applied to automate the first stage of resume screening.

It combines document parsing, information extraction, NLP similarity, rule-based matching, weighted scoring, ranking, explainability, and data export into a single application.

