class EmailPrompts:
    def create_email_prompt(
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
