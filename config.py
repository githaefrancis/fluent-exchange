import os



class Config:
  '''
  General class configuration
  '''
  SECRET_KEY=os.environ.get('SECRET_KEY')
  QUOTE_BASE_URL='https://api.quotable.io/random'

  SIMPLEMDE_JS_IIFE=True
  SIMPLEMDE_USE_CDN=True
  
  MAIL_SERVER='smtp.googlemail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
  SQLALCHEMY_DATABASE_URI='postgresql://postgres:bwbTZH0iPnpLNh3Mqleq@containers-us-west-199.railway.app:5488/railway'

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