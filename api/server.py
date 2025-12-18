from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(
    title="AI Researcher API",
    version="1.0",
    description="Jarvis ↔ AI Researcher bridge"
)

app.include_router(router)

# run:
# uvicorn api.server:app --host 0.0.0.0 --port 8000
