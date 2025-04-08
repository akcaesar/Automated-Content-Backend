# Automated-Content-Backend

This project takes some text input, and makes a short video/reel that can be saved or posted on youtube.


Overview:
Text input > summarize > fetch stock images and combine > voice over (with summarized content) > combine with stock images > save video or post on Youtube



Folder structure:
blog-to-video/
├── backend/
│   ├── src/
│   │   ├── core/              # Configuration and shared utilities
│   │   │   ├── config.py      # Environment variables
│   │   │   └── database.py    # DB connection (if needed)
│   │   ├── modules/
│   │   │   ├── summarization/ # AI text processing
│   │   │   │   ├── router.py
│   │   │   │   └── service.py
│   │   │   ├── tts/          # Text-to-speech module
│   │   │   ├── video/        # Video generation logic
│   │   │   └── uploads/      # Social media integration
│   │   ├── models/           # Pydantic schemas
│   │   ├── utils/            # Helper functions
│   │   └── main.py           # FastAPI app instance
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic/              # Database migrations
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/            # Next.js routes
│   │   ├── services/         # API clients
│   │   └── styles/
│   ├── package.json
│   └── next.config.js
├── scripts/                  # Deployment/utility scripts
└── .env                      # Environment variables
