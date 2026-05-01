import os
from langchain_google_genai import ChatGoogleGenerativeAI

print("1. Checking for Gemini API Key...")
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("❌ ERROR: GOOGLE_API_KEY is missing! Docker did not load your .env file.")
    exit()
else:
    print("✅ Key found in environment!")

print("\n2. Testing connection to Google Gemini...")
try:
    # Use the exact model name from my successful list
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.1)
    
    # Send a simple ping
    response = llm.invoke("Respond with exactly these words: 'Gemini API connection successful!'")
    
    print("\n🤖 AI Response:")
    print(response.content)
    
except Exception as e:
    print("\n❌ ERROR: Connection failed! Your key might be invalid.")
    print("Details:", e)