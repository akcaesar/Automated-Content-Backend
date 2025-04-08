"""
Author: Akshay NS

Contains: router for text to speech module

"""

import TTS.model
from fastapi import APIRouter, HTTPException

import TTS

router = APIRouter()

@router.post("/generate_audio/")
async def generate_audio(text: str):
    """Convert summary to AI-generated speech."""
    try:
        tts = TTS.model('"tts_models/en/ljspeech/glow-tts"')
        tts.tts_to_file(text, file_path="output_audio.wav")
        return {"audio_url": "/output_audio.wav"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
