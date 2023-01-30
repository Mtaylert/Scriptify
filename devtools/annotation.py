from app.resume_parsing.text_extration import ResumePageExtraction
import os

filpath = "/Users/home/workplace/Scriptify/test_data/test_resumes/"
resume_parser = {}
for file in os.listdir(filpath):
    first_section = {}
    full_path = filpath + file
    parsed_pdf_page = ResumePageExtraction().build_page(pdf_file=full_path)
    for page in parsed_pdf_page:
        cutoff = 5
        page_num = 1
        if page == page_num:
            for line in parsed_pdf_page[page]["text"]:
                if line <= cutoff:
                    text_line = parsed_pdf_page[page]["text"][line]
                    for token in text_line:
                        print(token)
                        my_input = ()
                        if my_input == "n":
                            first_section
            print()


