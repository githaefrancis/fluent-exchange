from flask import redirect, render_template,url_for,request,flash
from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from ..models import User,Role
from ..email import mail_message

@auth.route('/login', methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  login_form=LoginForm()
  if login_form.validate_on_submit():
    user=User.query.filter_by(email=login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user)
      flash(f'Welcome, {user.username}','success')
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password','error')


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
    mail_message("Welcome to Fluent Exchange","email/welcome",user.email,user=user)
    flash('Registration Successful, Welcome','success')
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',register_form=register_form)




@auth.route('/user/<user_name>/logout')
@login_required
def logout(user_name):
  logout_user()
  return redirect(url_for("main.index"))