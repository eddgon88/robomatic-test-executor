# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(Config):
    ENV = "local"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://robomatic:robomatic@localhost:5432/test_executor'                                
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'jdbc:postgresql://${DB_HOST}:${DB_PORT}/test_executor?stringtype=unspecified'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cloudacademy:pfm_2020@host.docker.internal:3306/order_dev'
    SQLALCHEMY_ECHO = True


