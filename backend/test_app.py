import unittest
import json
from app import app  # Import the Flask app from app.py

class FlaskTestCase(unittest.TestCase):
    # Set up test client
    def setUp(self):
        self.client = app.test_client()

    def test_chat(self):
        # Define the test data (user message)
        data = {'message': 'how is whether is sarnia'}

        # Make a POST request to the /chat route
        response = self.client.post('/chat', json=data)

        # Print the response for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Data: {response.data.decode('utf-8')}")

        # Assert the status code is 200
        self.assertEqual(response.status_code, 200)  # Check if the response code is 200

        # Assert that the response contains a 'response' key in the JSON response
        self.assertIn('response', response.json)  # Check if the response contains 'response' key

        # Optionally check if the response contains a non-empty message
        self.assertGreater(len(response.json['response'].strip()), 0, "Chatbot response is empty")

if __name__ == '__main__':
    unittest.main()
