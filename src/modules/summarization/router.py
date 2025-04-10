from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import re
from duckduckgo_search import DDGS
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

hftoken = os.getenv('HF_TOKEN')

# Hugging Face API Client
client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # can use any instruct model
    token= hftoken
)

# Define the input schema using Pydantic
class SummarizeRequest(BaseModel):
    topic: str

# Search & scrape utility
def search_and_extract(topic):
    with DDGS() as ddgs:
        results = list(ddgs.text(topic, max_results=1))
        if not results:
            return "Sorry Sir, I found nothing. The internet has failed us 😔."
        url = results[0]['href']

    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")

        # Clean page
        for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
            tag.decompose()

        main = soup.find("article") or soup.find("main") or soup.find("div", {"id": "mw-content-text"}) or soup.body
        text = main.get_text(separator="\n", strip=True)
        text = re.sub(r"\n{2,}", "\n\n", text)
        return text[:3000]  # truncate to stay under token limits
    except Exception as e:
        return f"Failed to fetch content, Sir: {e}"

# FastAPI endpoint
router = APIRouter()

@router.post("/summarize/")
async def funny_summary(request: SummarizeRequest):
    topic = request.topic  # Get the topic from the request body
    if not topic:
        raise HTTPException(status_code=400, detail="Sir, you must provide a topic.")
    
    raw_text = search_and_extract(topic)

    # Summarize and style it
    prompt = f"""
    Here's a boring explanation of '{topic}': 
    {raw_text}

    Now rewrite this in a engaging, and curious, mysterious tone. Strictly only mention the top 5. It should be too the point. No fluff.
    """
    response = client.text_generation(prompt, max_new_tokens=400)
    return {"funny_summary": response.strip()}
