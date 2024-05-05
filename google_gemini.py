from dotenv import load_dotenv
import os
load_dotenv()

import google.generativeai as genai
gemini_key = os.getenv("apikey")
genai.configure(api_key = gemini_key)

model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

def askgemini(prompt):
    return model.generate_content(prompt).text