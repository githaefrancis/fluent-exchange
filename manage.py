from app import create_app,db
from flask_migrate import Migrate
import unittest
app=create_app('development')

migrate=Migrate()

migrate.init_app(app,db)

@app.cli.command()
def test():
  '''
  Run unit tests
  '''
  tests=unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@app.shell_context_processor

def make_shell_context():
  return dict(app=app,db=db)
  


