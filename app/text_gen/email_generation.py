from app.text_gen.gpt_model import GPT3
from app.text_gen.prompt_tools import EmailPrompts


class EmailGeneration(EmailPrompts, GPT3):
    def __init__(self):
        super(EmailGeneration, self).__init__()

    def generate_email(
        self,
        intro_name: str,
        salutation_name: str,
        company_name: str,
        skill_desired: str,
        resume_context: str,
    ):
        prompt = self.basic_email_prompt(
            intro_name=intro_name,
            salutation_name=salutation_name,
            company_name=company_name,
            skill_desired=skill_desired,
            resume_context=resume_context,
        )

        response = self.generate_text(prompt=prompt)
        return response
