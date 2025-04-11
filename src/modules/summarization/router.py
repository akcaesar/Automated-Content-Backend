from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from .methods import search_and_extract
from dotenv import load_dotenv
import os

load_dotenv()
hftoken = os.getenv('HF_TOKEN')

# Hugging Face API Client
client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # can use any instruct model
    token= hftoken
)

# Define the input schema using Pydantic
class SummarizeRequest(BaseModel):
    topic: str

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

    Now rewrite this in a engaging, and curious tone. Strictly only mention the top 5. It should be too the point. No fluff.
    """
    response = client.text_generation(prompt, max_new_tokens=400)
    return {"funny_summary": response.strip()}
