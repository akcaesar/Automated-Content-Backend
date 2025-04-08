# """
# Author: Akshay NS

# Contains: router for loading the summarizer (bart) from transformers

# """


# from fastapi import APIRouter, HTTPException, Depends

# import httpx

# from transformers import pipeline

# router = APIRouter()

# # Load summarization model globally to avoid reloading it per request.
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


# @router.post("/summarize/")
# async def summarize_blog(url: str):
#     """Fetch and summarize a blog article."""
#     try:
#         response = httpx.get(url)
#         text = response.text[:1000]  # Simplified parsing, use BeautifulSoup if needed.
#         summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
#         return {"summary": summary[0]["summary_text"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # You can use other algorithms like LexRank or Luhn
import httpx

router = APIRouter()

# Define request and response schemas using Pydantic
class SummarizationRequest(BaseModel):
    url: str

class SummarizationResponse(BaseModel):
    summary: str

def summarize_text(text: str, sentence_count: int = 5) -> str:
    """Summarize text using Sumy."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()  # You can replace this with LexRankSummarizer or LuhnSummarizer
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

@router.post("/summarize/", response_model=SummarizationResponse)
async def summarize_blog(request: SummarizationRequest):
    """Fetch and summarize a blog article."""
    try:
        # Fetch blog content
        # response = httpx.get(request.url)
        # if response.status_code != 200:
        #     raise HTTPException(status_code=400, detail="Failed to fetch the blog content.")
        
        # # Extract text (simplified; use BeautifulSoup for better parsing)
        # text = response.text[:5000]  # Limit to first 5000 characters

        # # Summarize text using Sumy
        # summary = summarize_text(text, sentence_count=5)
        # return SummarizationResponse(summary=summary)
        return {"summary": "This is a placeholder summary."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

