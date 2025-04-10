"""
Author: Akshay NS

Contains: main entry point for fastapi application

"""
from fastapi import FastAPI

from modules.summarization import router as summarization_router
from modules.tts.router import router as tts_router
from modules.video.router import router as video_router

app = FastAPI()

app.include_router(summarization_router.router, tags=["Summarization"])
app.include_router(tts_router, tags=["Text-to-Speech"])
app.include_router(video_router, prefix="/video", tags=["Video Generation"])
