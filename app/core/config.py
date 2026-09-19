from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "local"
    service_name: str = "benyan-fastapi-starter"
    log_json: bool = False
    database_url: str = "postgresql+asyncpg://benyan:benyan_local@localhost:5432/benyan"


settings = Settings()
