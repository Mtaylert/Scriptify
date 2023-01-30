import pdfplumber
from typing import Dict

class ResumePageExtraction:
    def __init__(self, next_line_threshold=3):
        self.next_line_threshold = next_line_threshold

    def build_page(self, pdf_file: pdfplumber) -> Dict[str]:
        parsed_page_data = {"text": {}, "coordinates": {}}
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                words = page.extract_words()
                line_number = 0
                word_bottom_location = None
                for word in words:
                    coordinates = {
                        k: v
                        for k, v in word.items()
                        if k in ["x0", "x1", "top", "bottom"]
                    }
                    word_info = {"text": word["text"], "coordinates": coordinates}
                    bottom = word_info["coordinates"]["bottom"]
                    if not word_bottom_location:
                        word_bottom_location = bottom
                        for key, value in word_info.items():
                            parsed_page_data[key].setdefault(line_number, [])
                            parsed_page_data[key][line_number].append(value)
                    else:
                        if (
                            abs(word_bottom_location - bottom)
                            <= self.next_line_threshold
                        ):
                            for key, value in word_info.items():
                                parsed_page_data[key][line_number].append(value)
                            word_bottom_location = bottom
                        else:
                            line_number += 1
                            word_bottom_location = bottom
                            for key, value in word_info.items():
                                parsed_page_data[key].setdefault(line_number, [])
                                parsed_page_data[key][line_number].append(value)
        return parsed_page_data


path = "/Users/home/workplace/Scriptify/test_data/test_resumes/sourabh_bajaj_resume.pdf"

parsed_pdf_page = ResumePageExtraction().build_page(pdf_file=path)
print(parsed_pdf_page["text"])
