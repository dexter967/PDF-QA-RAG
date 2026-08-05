import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)

prompt = "Say hello in one short sentence."

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    print("\n✅ Gemini Response:\n")
    print(response.text)

except Exception as e:
    print("\n❌ Error:")
    print(e)