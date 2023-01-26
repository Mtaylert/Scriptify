class EmailPrompts:
    def create_email_prompt(self, intro_name: str, company_name: str, experience_type: str, salutation_name: str) -> str:

        intro = f"""You are a recruiter and your name is {intro_name} at {company_name} staffing agency. 
                    You are wondering if the candidate is open to hearing about a new job opportunity. You are very polite and personable. You also have strong technical writing skills. Generate an outreach email based upon 
                    the context below. Let them know the client is interested in hiring someone with strong {experience_type} experience. 
                    Let the candidate know that the have an impressive resume and experience. The candidates name is will appear at the top. Include the name {salutation_name} in the salutation. \n\n"""
        return intro
