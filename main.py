import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Generate content using Gemini API.")
parser.add_argument("user_prompt", type=str, help="The prompt to generate content for.")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

if response.usage_metadata:
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
else:
    raise RuntimeError("No usage metadata found in the response.")
