from flask import Flask
from config import config_options
from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

def create_app(config_name):
  app=Flask(__name__)
  app.config.from_object(config_options[config_name])


  app.register_blueprint(main_blueprint)

  app.register_blueprint(auth_blueprint)

  db.init_app(app)


  return app
