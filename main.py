import argparse
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Generate content using Gemini API.")
parser.add_argument("user_prompt", type=str, help="The prompt to generate content for.")
args = parser.parse_args()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=args.user_prompt,
)

if response.usage_metadata:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
else:
    raise RuntimeError("No usage metadata found in the response.")
