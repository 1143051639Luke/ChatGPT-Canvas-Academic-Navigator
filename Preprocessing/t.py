import sys
import os

major, minor, micro = sys.version_info[:3]
print(f"Your Python version is {major}.{minor}.{micro}")

api_key = os.environ["OPENAI_API_KEY"]
print(api_key)