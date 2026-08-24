import argparse,json
from pathlib import Path
import pandas as pd
from core.agent import ResumeScreeningAgent
from core.parsers import parse_text_file,parse_resume_file

p=argparse.ArgumentParser(); p.add_argument("--jd",required=True); p.add_argument("--resumes",required=True); p.add_argument("--output",default="output"); a=p.parse_args()
jdpath=Path(a.jd); out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
jd=parse_text_file(jdpath.name,jdpath.read_bytes())
cs=[parse_resume_file(x.name,x.read_bytes()) for x in sorted(Path(a.resumes).iterdir()) if x.suffix.lower() in {".pdf",".docx",".txt"}]
if not cs: raise SystemExit("No readable resumes found.")
r=ResumeScreeningAgent().screen(jd,cs)
rows=[]
for x in r:
    y=dict(x)
    for k in ["jd_skills","skills","matched_skills","missing_skills"]: y[k]=", ".join(y[k])
    rows.append(y)
pd.DataFrame(rows).to_csv(out/"ranked_candidates.csv",index=False)
(out/"ranked_candidates.json").write_text(json.dumps(r,indent=2,ensure_ascii=False),encoding="utf-8")
print(f"Screened {len(r)} resumes.")
for x in r: print(f"{x['rank']:>2}. {x['candidate_name']} — {x['final_score']:.2f}/100")
