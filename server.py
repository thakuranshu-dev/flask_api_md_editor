from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Set Gemini model
# gemini_model = genai.GenerativeModel('gemini-pro')
gemini_model = genai.GenerativeModel('gemini-2.0-flash')
print("Backend Server Started")
def query_gemini(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini Error:", e)
        return "Error getting response from Gemini."

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    text_data = data.get('text', '')
    userMsg = text_data
    response = query_gemini(userMsg)
    return jsonify({'solution': response})

if __name__ == '__main__':
    app.run(debug=True)