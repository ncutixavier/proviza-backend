# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# from sqlalchemy.orm import sessionmaker

# url = URL.create(
#     drivername="postgres",
#     username="postgres",
#     password="1234",
#     host="localhost",
#     database="proviza",
#     port=5432
# )

# engine = create_engine(url)
# Session = sessionmaker(bind=engine)
# session = Session()
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = './.env'


settings = Settings()
