import os



class Config:
  '''
  General class configuration
  '''
  SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG=True

class TestConfig(Config):
  pass

config_options={

  'development':DevConfig,
  'test':TestConfig,
  'production':ProdConfig
}