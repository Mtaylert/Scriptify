import uuid
from os import mkdir, path, remove

import PyPDF2
from fastapi import UploadFile

tempdir = "/tmp/resumes"


class PDFParser:
    async def extract_text_from_pdf(self, file: UploadFile) -> str:
        if not path.exists(tempdir):
            mkdir(tempdir)
        await save_file(file)
        pdf_text = []
        reader = PyPDF2.PdfReader(f"{tempdir}/{file.filename}", strict=False)
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
        return pdf_text[0]


async def save_file(file: UploadFile):
    tempdir = "/tmp/resumes"
    with open("{}/{}".format(tempdir, file.filename), "wb+") as temp:
        temp.write(file.file.read())
