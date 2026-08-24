# Scoring Method

Final score: **0–100**

- **45% NLP relevance:** TF-IDF cosine similarity between the complete JD and complete resume.
- **35% skill match:** matched JD skills divided by skills detected in the JD.
- **15% experience:** compares extracted years with the minimum years stated in the JD.
- **5% education:** checks whether the requested education level/degree appears in the resume.

Formula:

`0.45 × NLP + 0.35 × Skills + 0.15 × Experience + 0.05 × Education`

Ranking tie-breakers are skill score, NLP score, then candidate name.

Reasoning is generated only from extracted evidence. Protected/sensitive characteristics are not scoring features.

This is a deterministic local screening tool intended to support human review, not replace it.
