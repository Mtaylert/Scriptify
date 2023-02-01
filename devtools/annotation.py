from app.resume_parsing.text_extration import ResumePageExtraction
import os
import pandas as pd
import json
import re 
def parse():
    filpath = "/Users/home/workplace/Scriptify/test_data/test_resumes/"
    resume_parser = []
    for file in os.listdir(filpath):
        first_section = {}
        full_path = filpath + file
        parsed_pdf_page = ResumePageExtraction().build_page(pdf_file=full_path)
        for page in parsed_pdf_page:
            print("*********** NEW RESUME ***********")
            cutoff = 5
            page_num = 1
            if page == page_num:
                for line in parsed_pdf_page[page]["text"]:
                    if line <= cutoff:
                        annotation = {"text":[], "labels":[]}
                        text_line = parsed_pdf_page[page]["text"][line]
                        for token in text_line:
                            annotation['labels'].append('o')
                            annotation['text'].append(token.replace('\u200b', '').replace("\ue800",''))
                        resume_parser.append(annotation)
    with open('/Users/home/workplace/Scriptify/test_data/entity_annotation/entity_labeling.json', 'w') as file:
        file.write(json.dumps(resume_parser, indent=4))

def write_ton_jso():
    with open('entity_labeling_2.json', 'w') as file:
        for i in range(3):
            for i in df['Resume'].iloc[i][:200].split('\\n'):
                annotation = {"text":[], "labels":[]}
                for word in i.split(' '):
                    print(word)
                    my_input = input()
                    if my_input == "b":
                        annotation['text'].append(word)
                        annotation['labels'].append(my_input)
                    else:
                        annotation['text'].append(word)
                        annotation['labels'].append('o')
                file.write(json.dumps(annotation))
                file.write('\n')
        file.close()


parse()