import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
class Config:
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  
  



class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    

    DEBUG = True
