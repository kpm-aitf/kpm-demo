from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .settings import settings
from .workflow import router as workflow_router
from .dashboard import router as dashboard_router

app = FastAPI(title="Tim 4 RAG + MVP Backend")

# Izinkan frontend akses backend (CORS)
origins = [settings.app_referer] if settings.app_env == "production" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workflow_router)
app.include_router(dashboard_router)

@app.get("/health")
def health():
    return {"status": "ok"}