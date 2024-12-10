from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

CORS(app)

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


# Define the root route
@app.route('/')
def home():
    return "Welcome to the ChatBot API!"

# Define the route for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    # Get user message from the request
    user_message = request.json.get('message')

    # Check if the user sent a message
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Use the OpenAI API to get a response from the chatbot
    try:
        # Use the correct endpoint for chat completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use other models like gpt-4 as well
            messages=[{"role": "user", "content": user_message}]
        )

        # Extract the response text from the OpenAI API result
        chatbot_response = response['choices'][0]['message']['content'].strip()

        # Return the chatbot response
        return jsonify({'response': chatbot_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
