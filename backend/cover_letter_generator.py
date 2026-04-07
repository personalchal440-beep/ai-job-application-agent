import openai

# Function to generate a cover letter

def generate_cover_letter(job_title, company_name, user_name, user_experience, user_skills):
    prompt = f"Write a cover letter for {user_name} applying for the position of {job_title} at {company_name}.\n\nUser Experience:\n{user_experience}\n\nUser Skills:\n{user_skills}\n"  

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == '__main__':
    job_title = 'Software Engineer'
    company_name = 'Innovative Tech Solutions'
    user_name = 'John Doe'
    user_experience = '5 years of experience in software development, mainly focused on Python and Java.'
    user_skills = 'Python, Java, Team Leadership, Agile Development'

    cover_letter = generate_cover_letter(job_title, company_name, user_name, user_experience, user_skills)
    print(cover_letter)