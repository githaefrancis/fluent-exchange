import os
from flask import redirect, render_template,request,url_for
from flask_login import current_user, login_required
from . import main
from ..request import get_quote
from ..models import Post, User
from .forms import PostForm
from werkzeug.utils import secure_filename

@main.route('/')
def index():
  quote=get_quote()
  posts=Post.query.all()
  return render_template('index.html',quote=quote,posts=posts)


@main.route('/user/<user_name>/profile')
@login_required
def profile(user_name):
  user=User.query.filter_by(id=current_user.id).first()

  return render_template('profile/profile.html',user=user)

@main.route('/blog/write' , methods=['GET','POST'])
@login_required
def write():
  post_form=PostForm()

  if request.method=='POST':
    banner=request.files['banner']

    if banner:
      post_title=request.form.get('title')
      content=request.form.get('content')
      filename=secure_filename(banner.filename)
      banner.save(os.path.join('app/static/images',filename))
      file_path=f'images/{filename}'

      new_post=Post(title=post_title,content=content,user=current_user,banner_path=file_path)
      new_post.save_post()
      return redirect(url_for('main.index'))
  return render_template('write.html',post_form=post_form)


@main.route('/blog/post/<id>')
def blog_post(id):
  post=Post.query.filter_by(id=id).first()
  return render_template('post.html',post=post)