"""
Author: Akshay NS

Contains: router for moviepy editor

"""

from fastapi import APIRouter, BackgroundTasks, HTTPException

import moviepy.editor as mp

router = APIRouter()

@router.post("/generate_video/")
async def generate_video(summary: str, background_tasks: BackgroundTasks):
    """Combine images, narration, and subtitles into a video."""
    def process_video():
        try:
            audio_clip = mp.AudioFileClip("output_audio.wav")
            images = ["image1.jpg", "image2.jpg"]  # Replace with fetched images.
            clips = [mp.ImageClip(img).set_duration(2) for img in images]
            video = mp.concatenate_videoclips(clips).set_audio(audio_clip)
            video.write_videofile("output_video.mp4", fps=24)
        except Exception as e:
            print(f"Error generating video: {e}")

    background_tasks.add_task(process_video)
    return {"video_url": "/output_video.mp4"}
