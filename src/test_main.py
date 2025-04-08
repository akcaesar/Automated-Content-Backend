"""
Author: Akshay NS

Contains: test script for different functions within the app

"""

import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

# Test Summarization Endpoint
def test_summarize_blog():
    url = "https://www.theschooloflife.com/"  # Replace with a valid URL for testing
    response = client.post("/summarization/summarize/", json={"url": url})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) > 0

# # Test Text-to-Speech Endpoint
# def test_generate_audio():
#     text = "This is a sample text for testing TTS."
#     response = client.post("/tts/generate_audio/", json={"text": text})
#     assert response.status_code == 200
#     assert "audio_url" in response.json()

# # Test Video Generation Endpoint
# def test_generate_video():
#     summary = "This is a sample summary for testing video generation."
#     response = client.post("/video/generate_video/", json={"summary": summary})
#     assert response.status_code == 200
#     assert "video_url" in response.json()
