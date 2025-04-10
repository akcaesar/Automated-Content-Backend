"""
Author: Akshay NS

Contains: router for text to speech module using gTTS (Google Text-to-Speech)

"""

from fastapi import APIRouter, HTTPException
from gtts import gTTS
from pydantic import BaseModel


router = APIRouter()


class TextRequest(BaseModel):
    text: str

@router.post("/generate_audio/")
async def generate_audio(request: TextRequest):
    """Convert summary to AI-generated speech using gTTS."""
    text = request.text
    try:
        # Check if text is provided
        if not text:
            raise HTTPException(status_code=400, detail="Text is required to generate speech.")

        # Convert the text to speech using gTTS
        tts = gTTS(text=text, lang='en', slow=False)

        # Save the speech as an audio file
        output_audio_path = "output_audio.mp3"
        tts.save(output_audio_path)

        # Return the URL to access the generated audio
        return {"audio_url": f"/{output_audio_path}"}

    except Exception as e:
        # Catch any exceptions and return an internal server error
        raise HTTPException(status_code=500, detail=str(e))
