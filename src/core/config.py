"""
Author: Akshay NS

Contains: shared configurations

"""



from pydantic import BaseSettings

class Settings(BaseSettings):
    unsplash_access_key: str = "your_unsplash_api_key"
    coqui_tts_model: str = "tts_models/en/ljspeech/glow-tts"
    youtube_api_key: str = "your_youtube_api_key"
    tiktok_access_token: str = "your_tiktok_api_token"

settings = Settings()
