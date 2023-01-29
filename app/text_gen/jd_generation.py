from typing import List, Optional

from app.text_gen.gpt_model import GPT3
from app.text_gen.prompt_tools import JDPrompts


class JDGeneration(JDPrompts, GPT3):
    def __init__(self):
        super(JDGeneration, self).__init__()

    def generate_job_description(
        self,
        company_name: str,
        position_title: str,
        location: str,
        requirements: List[str],
        placement_company: Optional[str],
    ):
        prompt = self.basic_jd_prompt(
            company_name=company_name,
            position_title=position_title,
            location=location,
            requirements=requirements,
            placement_company=placement_company,

        )
        intro_response = (
            " ".join(self.generate_text(prompt=prompt.get("intro"))).lstrip()
            + f"\n {position_title} – Skills, Expertise & Experience Requirements: \n"
        )
        requirement_list = self.generate_text(prompt=prompt.get("requirements"))
        return {"intro": intro_response, "requirements": requirement_list}
