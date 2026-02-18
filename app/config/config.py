from dotenv import load_dotenv
import os
env_name = os.getenv("ENV_NAME","prod")
load_dotenv()

class Config:
    FROM_EMAIL= os.getenv("FROM_EMAIL")
    TO_EMAIL= os.getenv("TO_EMAIL")
    APP_PASSWORD= os.getenv("APP_PASSWORD")
    EMAIL_HOST= os.getenv("EMAIL_HOST")
    EMAIL_PORT= int(os.getenv("EMAIL_PORT"))

class Dev(Config):
    DEBUG = True

class Prod(Config):
    DEBUG = False

config = {"dev":Dev,"prod":Prod}