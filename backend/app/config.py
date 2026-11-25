from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):

    APP_NAME: str = "NOVA"
    APP_VERSION: str = "0.1.0"

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    DEBUG: bool = True

    WORKSPACE_DIR: Path = PROJECT_ROOT / "workspace"
    DATA_DIR: Path = PROJECT_ROOT / "data"
    LOG_DIR: Path = PROJECT_ROOT / "logs"

    DATABASE_URL: str = (
        f"sqlite+aiosqlite:///{DATA_DIR / 'nova.db'}"
    )

    MAX_TOOL_CALLS: int = 40
    MAX_RETRIES: int = 3

    MAX_EXECUTION_TIME: int = 600

    MAX_FILE_SIZE: int = 2_000_000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()


settings.WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
settings.DATA_DIR.mkdir(parents=True, exist_ok=True)
settings.LOG_DIR.mkdir(parents=True, exist_ok=True)
