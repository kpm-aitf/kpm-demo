import os
from pathlib import Path
from dotenv import load_dotenv

_env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=_env_path if _env_path.exists() else None)


class Settings:
    # OpenRouter
    openrouter_api_key: str       = os.getenv("OPENROUTER_API_KEY", "")
    openrouter_base_url: str      = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1/chat/completions")
    openrouter_model: str         = os.getenv("OPENROUTER_MODEL", "google/gemma-3-4b-it:free")
    openrouter_max_tokens: int    = int(os.getenv("OPENROUTER_MAX_TOKENS", "1500"))
    openrouter_timeout: int       = int(os.getenv("OPENROUTER_TIMEOUT", "60"))

    # Default temperatures
    temperature_default: float    = float(os.getenv("TEMPERATURE_DEFAULT", "0.7"))
    temperature_revise: float     = float(os.getenv("TEMPERATURE_REVISE", "0.6"))
    temperature_chat: float       = float(os.getenv("TEMPERATURE_CHAT", "0.75"))

    # App
    app_env: str                  = os.getenv("APP_ENV", "development")
    app_referer: str              = os.getenv("APP_URL", "http://localhost:3000")
    app_title: str                = os.getenv("APP_TITLE", "KPM AITF Platform")

    # Chat
    chat_history_limit: int       = int(os.getenv("CHAT_HISTORY_LIMIT", "6"))


settings = Settings()
