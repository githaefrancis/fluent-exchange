from . import main


@main.route('/')
def index():
  return '<h1>Welcome to the fluent app</h1>'