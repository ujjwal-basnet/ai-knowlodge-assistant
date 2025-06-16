from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ollama_url: str
    model_name: str
    embedding_model: str
    chroma_path: str
    mlflow_tracking_url: str

    model_config = SettingsConfigDict(env_file=".env")

s = Settings()
