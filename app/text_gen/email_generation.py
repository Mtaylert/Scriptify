import openai

from app.text_gen.prompt_tools import EmailPrompts
from app.text_gen.pdf_to_text import PDFParser
from app.config import settings

class EmailGeneration(EmailPrompts):
    def __init__(self, intro_name, salutation_name, company_name, skill):
        self.intro_name = intro_name
        self.salutation_name = salutation_name
        self.comapny_name = company_name
        self.skill = skill
        super(EmailGeneration, self).__init__()
    def generate_email(self):
        openai.api_key = settings.API_KEY
        prompt = self.create_email_prompt(intro_name=self.intro_name, salutation_name=self.salutation_name, company_name=self.comapny_name, experience_type=self.skill)
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = prompt,
            temperature = 0.6,
            max_tokens = 500
        )
        email = response.choices[0].text.split('\n')
        return email
