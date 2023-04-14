from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    MODE = os.getenv('MODE')
    MYSQL_HOST = "mysql" if MODE == 'PROD' else "127.0.0.1"
    REDIS_HOST = "redis" if MODE == 'PROD' else "127.0.0.1"
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:123456@{MYSQL_HOST}:3306/fastapi_db"


settings = Settings()
