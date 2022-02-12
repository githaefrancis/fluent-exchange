from flask import redirect, render_template,url_for
from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from ..models import User,Role

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
    name_input=register_form.name.data
    email_input=register_form.email.data
    username_input=register_form.username.data
    password_input=register_form.password.data
    user_role=Role.query.filter_by(name='User').first()
    user=User(name=name_input,email=email_input,username=username_input,password=password_input,role=user_role)
    user.save_user()
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',register_form=register_form)