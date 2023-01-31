from app.resume_parsing.text_extration import ResumePageExtraction
import os
import re
import spacy

nlp = spacy.load('en_core_web_sm')

def email_extract(line):
    match = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", line)
    match = match.group(0) if match else None
    return match


def phone_number_extract(line):
    match = re.search(
        r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))",
        line,
    )
    match = match.group(0) if match else None
    return match


def get_name(line):
    doc = nlp(line)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return name


def section_one_parse(filepath):
    resume_parser = {}
    for file in os.listdir(filepath):
        first_section = {"name": None, "email": None, "phone": None, "Summary": None}
        full_path = filepath + file
        parsed_pdf_page = ResumePageExtraction().build_page(pdf_file=full_path)
        for page in parsed_pdf_page:
            for line in parsed_pdf_page[page]["text"]:
                text_line = " ".join(parsed_pdf_page[page]["text"][line])
                email = email_extract(text_line)
                phone = phone_number_extract(text_line)
                name = get_name(text_line)
                if email:
                    first_section["email"] = {"text": email, "confidence": 1}
                if phone:
                    first_section["phone"] = {"text": phone, "confidence": 1}
                if name:
                    first_section["name"] = {"text": name, "confidence": 1}
                resume_parser[file] = first_section
    return resume_parser



parsed_resumes = section_one_parse(filepath="/Users/home/workplace/Scriptify/test_data/test_resumes/")
print(parsed_resumes)