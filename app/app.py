from typing import Optional
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile

from app.text_gen.email_generation import EmailGeneration
from app.text_gen.pdf_to_text import PDFParser

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


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
