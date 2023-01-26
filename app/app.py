from fastapi import FastAPI, File, HTTPException, UploadFile
import uvicorn
from io import BytesIO


from app.text_gen.pdf_to_text import PDFParser
from app.text_gen.email_generation import EmailGeneration


app = FastAPI()

@app.get("/")
def health():
    return {"Scriptify":"Health"}


@app.post("/email_generation")
async def generate_email(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail='Bad file type')
    data = await PDFParser().extract_text_from_pdf(file=file)
    email  = EmailGeneration().generate_email()

    return {"pdf_text": data}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1",port=8080)