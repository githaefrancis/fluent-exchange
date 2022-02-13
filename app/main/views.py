from flask import render_template
from flask_login import current_user, login_required
from . import main
from ..request import get_quote
from ..models import User
from .forms import PostForm

@main.route('/')
def index():
  quote=get_quote()
  return render_template('index.html',quote=quote)


@main.route('/user/<user_name>/profile')
@login_required
def profile(user_name):
  user=User.query.filter_by(id=current_user.id).first()

  return render_template('profile/profile.html',user=user)

@main.route('/blog/write')
@login_required
def write():
  post_form=PostForm()
  return render_template('write.html',post_form=post_form)