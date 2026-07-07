from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password : str
    database_name: str
    database_username: str


    secretkey: str
    algorithm: str
    access_token_expire_minutes: int = 60

    model_config = ConfigDict(env_file=".env")

    # class config:
    #     env_file = ".env"  # in previous pydantic package this method is used

settings = Settings()