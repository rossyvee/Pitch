import os
class Config:
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  
  



class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    

    DEBUG = True
