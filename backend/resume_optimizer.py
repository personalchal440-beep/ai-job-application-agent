import openai

class ResumeOptimizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def extract_keywords(self, resume_text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Extract keywords from the following resume:
                    \n\n{resume_text}"
                }
            ]
        )
        keywords = response.choices[0].message['content'].strip().split('\n')
        return keywords

    def optimize_resume(self, resume_text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Optimize the following resume:
                    \n\n{resume_text}"
                }
            ]
        )
        optimized_resume = response.choices[0].message['content'].strip()
        return optimized_resume

# Example usage:
# optimizer = ResumeOptimizer(api_key="your_openai_api_key")
# keywords = optimizer.extract_keywords("Your resume text here...")
# optimized = optimizer.optimize_resume("Your resume text here...")