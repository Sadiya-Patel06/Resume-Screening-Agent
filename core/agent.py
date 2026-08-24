from core.scorer import nlp,skill_score,exp_score,edu_score,min_exp

class ResumeScreeningAgent:
    def screen(self,jd,candidates):
        req=min_exp(jd); out=[]
        for c in candidates:
            ns=nlp(jd,c["text"]); ss,jds,rs,matched,missing=skill_score(jd,c["text"])
            es=exp_score(c["experience_years"],req); ed=edu_score(jd,c["education_summary"],c["text"])
            total=.45*ns+.35*ss+.15*es+.05*ed
            strengths=[]; gaps=[]
            if ns>=60: strengths.append("strong NLP relevance")
            elif ns>=35: strengths.append("moderate NLP relevance")
            else: gaps.append("low NLP relevance")
            if ss>=70: strengths.append(f"strong skill coverage ({len(matched)} matched)")
            elif ss>=40: strengths.append(f"partial skill coverage ({len(matched)} matched)")
            else: gaps.append("limited direct skill coverage")
            if req is not None:
                if c["experience_years"] is not None and c["experience_years"]>=req: strengths.append(f"meets the {req:g}-year requirement")
                elif c["experience_years"] is None: gaps.append("experience could not be verified")
                else: gaps.append(f"below the {req:g}-year requirement")
            if ed==100: strengths.append("education appears to match")
            else: gaps.append("education requirement was not matched")
            reason=f"**{total:.2f}/100.** Strengths: {('; '.join(strengths) or 'none identified')}. Gaps: {('; '.join(gaps) or 'none identified')}."
            if missing: reason+=f" Missing JD skills: {', '.join(missing)}."
            out.append({**c,"final_score":total,"nlp_score":ns,"skill_score":ss,"experience_score":es,
                        "education_score":ed,"jd_skills":jds,"skills":rs,"matched_skills":matched,
                        "missing_skills":missing,"reasoning":reason,
                        "experience_years_display":f"{c['experience_years']:.1f} years" if c["experience_years"] is not None else "Not explicitly stated"})
        out.sort(key=lambda x:(-x["final_score"],-x["skill_score"],-x["nlp_score"],x["candidate_name"].lower()))
        for i,x in enumerate(out,1): x["rank"]=i
        return out
