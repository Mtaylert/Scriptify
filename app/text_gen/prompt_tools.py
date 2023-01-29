from typing import List, Optional


class EmailPrompts:
    def basic_email_prompt(
        self,
        intro_name: str,
        company_name: str,
        skill_desired: str,
        salutation_name: str,
        resume_context: str,
    ) -> str:

        intro = f"""You are a recruiter and your name is {intro_name} at {company_name} staffing agency.  Generate an outreach email based upon 
                    the context below. You are wondering if the candidate is open to hearing about a new job opportunity. You are very polite and personable. You also have strong technical writing skills. 
                     Let them know the client is interested in hiring someone with strong {skill_desired} experience. Summarize their skills to make it seem personal.
                    Let the candidate know that they have an impressive resume and experience. The candidate's name is at the top of the context. Include the name {salutation_name} in the salutation. \n\n"""
        resume_context = f"CONTEXT: {resume_context} \n\n"
        response = f"ANSWER:"
        prompt = intro + resume_context + response
        return prompt


class JDPrompts:
    def basic_jd_prompt(self, company_name: str, position_title: str, location: str, requirements: str, placement_company: Optional[str] = None):
        if placement_company:
            intro_summary = f"""You are a staffing agency and your company name is {company_name}. Write a brief job description about your client {placement_company} who is 
            seeking an experienced {position_title} in the {location} area.\n\n 
            """
        else:
            intro_summary = f"""You are a staffing agency and your company name is {company_name}. You are very enthusiastic. Write a short introduction that your company is 
        looking for an experienced {position_title} for your client located in {location}.\n\n 
        """
        intro_response = f"ANSWER: "
        intro_prompt = intro_summary + intro_response

        requirement_intro = f"""Write a bulleted list based on the context below. \n\n"""
        requirements_context = f"CONTEXT: {requirements} \n\n"
        requirements_reponse = f"ANSWER: "
        requirement_prompt = requirement_intro + requirements_context + requirements_reponse
        return {'intro': intro_prompt, "requirements" : requirement_prompt}
    
