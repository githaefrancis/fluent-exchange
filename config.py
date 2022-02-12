import os



class Config:
  '''
  General class configuration
  '''
  SECRET_KEY=os.environ.get('SECRET_KEY')
  QUOTE_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/fluent_exchange'
  DEBUG=True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/fluent_exchange'
  

config_options={

  'development':DevConfig,
  'test':TestConfig,
  'production':ProdConfig
}