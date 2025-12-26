from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    LLM_API_KEY: str = Field(..., description="API key for Inference")
    LLM_API_URL: str = Field(..., description="API Endpoint")

    LLM_MODEL_NAME: str = Field(default="alibaba-qwen3-32b", description="The specific model to use")

    APP_NAME: str = "Loom"
    DEBUG_MODE: bool = False

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore"
    )


try:
    settings = Settings()
except Exception as e:
    print(f"Configuration Error: {e}")
    exit(1)
