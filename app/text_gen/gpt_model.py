import openai
from app.config import local_settings


class GPT3:
    def generate_text(self, prompt: str):
        openai.api_key = local_settings.API_KEY
        response = openai.Completion.create(
            engine="text-davinci-002", prompt=prompt, temperature=0.6, max_tokens=500
        )
        return response.choices[0].text.split("\n")
