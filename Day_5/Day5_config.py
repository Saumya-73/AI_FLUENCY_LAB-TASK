
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Find the .env file in the main project folder
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

PROVIDER = "groq"
BASE_URL = "https://api.groq.com/openai/v1"
MODEL = "openai/gpt-oss-20b"

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY not found in the main project .env file")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)
