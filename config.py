from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/fastapi_db"
    redis_host = "127.0.0.1"


settings = Settings()
