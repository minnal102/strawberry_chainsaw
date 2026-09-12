import os
import sys

print("--- DIAGNOSTIC TEST ---")

# 1. Test Python libraries
print("\n[1/2] Checking Python libraries...")
try:
    import flask
    import flask_cors
    from google import genai
    print("  ✅ Flask, flask-cors, and google-genai are installed!")
except ImportError as e:
    print(f"  ❌ Missing library: {e}")
    sys.exit(1)

# 2. Test Gemini API key
print("\n[2/2] Checking Gemini API connection...")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("  ❌ API Key missing! Set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

try:
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-2.5-flash")
    response = chat.send_message("Say 'System Operational!'")
    print(f"  ✅ API Success! Response from Gemini: {response.text.strip()}")
    print("\n--- ALL TESTS PASSED! ---")
except Exception as e:
    print(f"  ❌ API Error: {e}")
    sys.exit(1)