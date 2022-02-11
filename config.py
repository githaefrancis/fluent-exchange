import os



class Config:
  '''
  General class configuration
  '''
  SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/fluent_exchange'
  DEBUG=True

class TestConfig(Config):
  pass

config_options={

  'development':DevConfig,
  'test':TestConfig,
  'production':ProdConfig
}