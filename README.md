# Automated-Content-Backend

This project takes some text input, and makes a short video/reel that can be saved or posted on youtube.


Overview:
Text input > summarize > fetch stock images and combine > voice over (with summarized content) > combine with stock images > save video or post on Youtube



Folder structure:
backend/
├── src/
│   ├── core/              # Configuration and shared utilities
│   │   ├── config.py      # Environment variables and settings
│   └── modules/           # Feature-specific modules (summarization, TTS, video generation)
│       ├── summarization/ # Summarization logic
│       │   ├── router.py  # API routes for summarization
│       │   └── service.py # Business logic for summarization
│       ├── tts/           # Text-to-speech logic
│       │   ├── router.py  # API routes for TTS
│       │   └── service.py # Business logic for TTS
│       ├── video/         # Video generation logic
│       │   ├── router.py  # API routes for video generation
│       │   └── service.py # Business logic for video generation
│   ├── utils/             # Helper functions (e.g., image fetching)
│   ├── models/            # Pydantic models for request validation
│   └── main.py            # FastAPI app entry point
└── requirements.txt       # Python dependencies
