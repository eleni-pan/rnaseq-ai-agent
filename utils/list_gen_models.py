import os
import google.generativeai as genai

# 1. Setup the API Key
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

print("Fetching available models from Google...")

try:
    # 2. List all available models
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Model Name: {m.name} | Display: {m.display_name}")
            
except Exception as e:
    print(f"❌ Error fetching models: {e}")
