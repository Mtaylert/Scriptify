import openai

from app.config import local_settings
from app.text_gen.prompt_tools import EmailPrompts


class EmailGeneration(EmailPrompts):
    def __init__(self):
        super(EmailGeneration, self).__init__()

    def generate_email(self, intro_name: str, salutation_name: str, company_name: str, skill_desired: str, resume_context: str):
        openai.api_key = local_settings.API_KEY
        prompt = self.create_email_prompt(
            intro_name=intro_name,
            salutation_name=salutation_name,
            company_name=company_name,
            skill_desired=skill_desired,
            resume_context=resume_context,
        )
        
        response = openai.Completion.create(
            engine="text-davinci-002", prompt=prompt, temperature=0.6, max_tokens=500
        )
        return response.choices[0].text.split('\n')
