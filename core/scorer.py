import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS=["python","java","javascript","typescript","c","c++","c#","sql","postgresql","mysql","mongodb","redis","html","css","react","angular","vue","node.js","node","flask","django","fastapi","spring","git","github","docker","kubernetes","aws","azure","gcp","machine learning","deep learning","natural language processing","nlp","generative ai","gen ai","llm","large language model","rag","retrieval augmented generation","langchain","transformers","pytorch","tensorflow","scikit-learn","pandas","numpy","matplotlib","power bi","tableau","excel","dax","data analysis","data analytics","statistics","computer vision","opencv","keras","rest api","restful api","api","microservices","linux","spark","hadoop","airflow","gitlab","jenkins","firebase","android","flutter","postman","ocr","prompt engineering"]

def has(text,skill):
    return bool(re.search(rf"(?<![a-z0-9]){re.escape(skill)}(?![a-z0-9])",text)) if skill in {"c","c++","c#"} else skill in text

def skills(text):
    t=text.lower(); out=[s for s in SKILLS if has(t,s)]
    if "node.js" in out and "node" in out: out.remove("node")
    if "generative ai" in out and "gen ai" in out: out.remove("gen ai")
    return sorted(set(out))

def min_exp(jd):
    vals=[float(m.group(1)) for m in re.finditer(r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)(?:\s+of)?\s*(?:relevant\s+|professional\s+)?experience",jd,re.I)]
    vals += [float(m.group(1)) for m in re.finditer(r"(?:minimum|at least)\s*(\d+(?:\.\d+)?)\s*(?:years?|yrs?)",jd,re.I)]
    return max(vals) if vals else None

def nlp(jd,resume):
    v=TfidfVectorizer(stop_words="english",ngram_range=(1,2)).fit_transform([jd,resume])
    return float(cosine_similarity(v[0:1],v[1:2])[0][0]*100)

def skill_score(jd,resume):
    j=set(skills(jd)); r=set(skills(resume)); m=sorted(j&r); miss=sorted(j-r)
    return (len(m)/len(j)*100 if j else 100),sorted(j),sorted(r),m,miss

def exp_score(x,req):
    if req is None: return 100 if x is not None else 50
    if x is None: return 0
    return min(x/req,1)*100

def edu_score(jd,edu,resume):
    j=jd.lower(); r=(edu+" "+resume).lower()
    req=[x for x in ("phd","doctorate","master","m.tech","mtech","m.e.","mba","bachelor","b.tech","btech","b.e.","b.sc","bsc","m.sc","msc","diploma") if x in j]
    return 100 if not req or any(x in r for x in req) else 0
