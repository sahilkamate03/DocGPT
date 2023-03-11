from dotenv import load_dotenv
import os

load_dotenv()
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

import openai

openai.api_key = OPEN_AI_API_KEY
model = "ada:ft-personal-2023-03-11-04-32-54"

keep = True
while (keep):
    prompt = input("Ask: ")
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.91,
        top_p=1.0,
        max_tokens=200,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print("Ans: ", response.choices[0].text.strip())
    print()