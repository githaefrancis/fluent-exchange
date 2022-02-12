from flask import redirect, render_template,url_for
from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from ..models import User

@auth.route('/login')
def login():
  login_form=LoginForm()
  return render_template('auth/login.html',login_form=login_form)


@auth.route('/register',methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  register_form=RegistrationForm()
  
  if register_form.validate_on_submit():
    user=User(name=register_form.name.data,email=register_form)
    user.save_user()
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',register_form=register_form)