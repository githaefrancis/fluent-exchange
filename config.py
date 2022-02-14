import os



class Config:
  '''
  General class configuration
  '''
  SECRET_KEY=os.environ.get('SECRET_KEY')
  QUOTE_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'

  SIMPLEMDE_JS_IIFE=True
  SIMPLEMDE_USE_CDN=True
  
  MAIL_SERVER='smtp.googlemail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
  

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/fluent_exchange'
  DEBUG=True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/fluent_exchange_test'
  

config_options={

  'development':DevConfig,
  'test':TestConfig,
  'production':ProdConfig
}