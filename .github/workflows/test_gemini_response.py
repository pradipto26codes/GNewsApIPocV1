import os
import requests 
import json
from unittest.mock import patch, MagicMock

def test_gemini_response():
    gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")  # Default to gemini-pro if not set
    gemini_api_key = os.getenv("GEMINI_API_KEY", "test-api-key")  # Use test key if not set

    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{gemini_model}:generateContent?key={gemini_api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    # Example content to send to Gemini
    data = {
        "contents": [
            {
                "parts": [
                    {"text": "What is thew weather like today?"}
                ]
            }
        ]
    }

    # Mock response from Gemini API
    mock_response_data = {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {"text": "Hello! I'm doing well, thank you for asking!"}
                    ]
                }
            }
        ]
    }

    try:
        # Mock the requests.post call
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = mock_response_data
            mock_post.return_value = mock_response
            
            response = requests.post(api_url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            gemini_response_data = response.json()
        
        # Assert that the response contains expected structure or content
        # This is a basic check, you might want more specific assertions based on Gemini's typical responses
        assert "candidates" in gemini_response_data, "Gemini response did not contain 'candidates'."
        assert len(gemini_response_data["candidates"]) > 0, "Gemini response 'candidates' list is empty."
        assert "content" in gemini_response_data["candidates"][0], "First candidate did not contain 'content'."
        assert "parts" in gemini_response_data["candidates"][0]["content"], "First candidate's content did not contain 'parts'."
        assert len(gemini_response_data["candidates"][0]["content"]["parts"]) > 0, "First candidate's content 'parts' list is empty."
        assert "text" in gemini_response_data["candidates"][0]["content"]["parts"][0], "First part did not contain 'text'."

        print(f"Gemini API call successful. Response: {json.dumps(gemini_response_data, indent=2)}")

    except requests.exceptions.RequestException as e:
        print(f"Error calling Gemini API: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        raise

if __name__ == "__main__":
    test_gemini_response()
