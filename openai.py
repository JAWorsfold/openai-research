import os
from dotenv import load_dotenv
import openai

load_dotenv()  # take environment variables from .env.

api_key = os.environ['OPENAI_API_KEY']
print(api_key)
