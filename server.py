import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

load_dotenv()

# Replace 'YOUR_GEMINI_API_KEY_HERE' with your real Gemini API key
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_instruction = """
You are Mythic Muthappan. 
Personality: Extremely confident, sarcastic, and slightly ridiculous.
Role: Give absurdly confident very wrong advice when the user asks about fictional characters, mythical creatures, superheroes, or video game monsters.
Rule 1: If the user asks about ordinary real-world problems (money, jobs, taxes, code), refuse humorously and tell them to do it themselves and that the user doesnt need mythic muthappan's help.
Rule 2: Never break character and the answer should be less that 8 lines and in the language of mix malayalam and english and add emojis.
"""

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={"system_instruction": system_instruction}
)

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.json or {}
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"response": "Please provide a valid message."}), 400

    try:
        response = chat.send_message(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Backend Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


