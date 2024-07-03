from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings class
    """

    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"
        from_attributes = True

