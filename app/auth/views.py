from . import auth


@auth.route('/login')
def login():
  return 'hello'


@auth.route('/register')
def register():
  return 'register'