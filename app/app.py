from typing import Optional, List
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi import Query

from app.text_gen.email_generation import EmailGeneration
from app.text_gen.pdf_to_text import PDFParser
from app.text_gen.jd_generation import JDGeneration

app = FastAPI(
    title="Scriptify Rest",
    description="REST API for Scriptify",
    version="1.0.0",
)


@app.get("/")
def health():
    return {"Scriptify": "Healthy"}


@app.post("/email_generation")
async def generate_email(
    intro_name: str,
    salutation_name: str,
    skill_desired: str,
    company_name: str,
    file: UploadFile = File(...),
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Bad file type")
    resume = await PDFParser().extract_text_from_pdf(file=file)
    email = EmailGeneration().generate_email(
        intro_name=intro_name,
        salutation_name=salutation_name,
        skill_desired=skill_desired,
        company_name=company_name,
        resume_context=resume,
    )
    return {"pdf_text": resume, "email": email}


@app.post("/job_description")
async def generate_job_description(
    company_name: str,
    position_title: str,
    location: str,
    requirements: str,
    placement_company : Optional[str],
):
    jd = JDGeneration().generate_job_description(
        company_name=company_name,
        position_title=position_title,
        location=location,
        requirements=requirements,
        placement_company=placement_company,
    )
    return {"job_description": jd}


@app.post("/resume_fraud")
async def generate_email(
    file: UploadFile = File(...),
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Bad file type")
    resume = await PDFParser().extract_text_from_pdf(file=file)
    out = {"prediction": "Not Fraud", "Confidence": 0.9764}
    return out


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
