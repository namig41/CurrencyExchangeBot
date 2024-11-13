from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_EXCHANGE_RATE: str

    TELEGRAM_TOKEN: str
    TELEGRAM_WEBHOOK_HOST: str
    TELEGRAM_WEBHOOK_PATH: str
    TELEGRAM_BOT_NAME: str

    @property
    def TELEGRAM_WEB_HOOK(self) -> str:
        return f"{self.TELEGRAM_WEBHOOK_HOST}{self.TELEGRAM_WEBHOOK_PATH}"


config = Settings()
