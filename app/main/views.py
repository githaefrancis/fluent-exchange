
import os

from flask import redirect, render_template,request,url_for,flash
from flask_login import current_user, login_required
from . import main
from ..request import get_quote
from ..models import Post, User,Comment,Subscriber
from .forms import PostForm,CommentForm,SubscribeForm
from werkzeug.utils import secure_filename
from .. import db
from ..request import subscriber_alert
from .request import fetch_comments_count

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','gif'}


@main.route('/',methods=['GET','POST'])
def index():
  quote=get_quote()
  posts=Post.query.filter_by(status='active').order_by(Post.id.desc()).all()
  subscriber_form=SubscribeForm()
  if request.method=='POST':
    if subscriber_form.validate_on_submit():
      new_subscriber=Subscriber(name=subscriber_form.name.data,email=subscriber_form.email.data)
      new_subscriber.save_subscriber()
      flash('You have subscribed successfully','success')
      return redirect(request.referrer)
  all_comments=fetch_comments_count(posts)
  return render_template('index.html',quote=quote,posts=posts,subscriber_form=subscriber_form,comments=all_comments)


@main.route('/user/<user_name>/profile')
@login_required
def profile(user_name):
  user=User.query.filter_by(id=current_user.id).first()
  posts=Post.query.filter_by(user=current_user,status='active').all()
  return render_template('profile/profile.html',user=user,posts=posts)

@main.route('/blog/write' , methods=['GET','POST'])
@login_required
def write():
  post_form=PostForm()
  if request.method=='POST':
    subscribers_list=Subscriber.query.filter_by(active=True).all()

    banner=request.files['banner']

    if banner:
      post_title=request.form.get('title')
      content=request.form.get('content')
      filename=secure_filename(banner.filename)
      banner.save(os.path.join('app/static/images',filename))
      file_path=f'images/{filename}'

      new_post=Post(title=post_title,content=content,user=current_user,banner_path=file_path)
      new_post.save_post()
      saved_post=Post.query.filter_by(user=current_user).order_by(Post.id.desc()).first()
      flash('Post created successfully','success')
      
      subscriber_alert(subscribers_list,saved_post)
      return redirect(url_for('main.blog_post',id=saved_post.id))
  return render_template('write.html',post_form=post_form)


@main.route('/blog/post/<id>',methods=['GET','POST'])
def blog_post(id):
  post=Post.query.filter_by(id=id).first()
  comment_form=CommentForm()
  comments=Comment.query.filter_by(post=post,status='active').all()
  if current_user.is_authenticated:
    comment_owner=current_user
  
  else:
    comment_owner=User.query.filter_by(username='guest').first()
  if request.method=='POST':
    comment=comment_form.comment.data
    new_comment=Comment(content=comment,user=comment_owner,post=post)
    new_comment.save_comment()
    return redirect(request.referrer)
  return render_template('post.html',post=post,comment_form=comment_form,comments=comments)


@main.route('/blog/post/<id>/delete')
def delete(id):
  post_to_delete=Post.query.filter_by(id=id).first()
  post_to_delete.delete_post()
  flash('Post Deleted successfully')
  return redirect(url_for('main.index'))

@main.route('/blog/post/<id>/update',methods=['GET','POST'])
def update(id):
  target_post=Post.query.filter_by(id=id).first()
  edit_post_form=PostForm(obj=target_post)
  # edit_post_form.title.data=target_post.title
  # edit_post_form.content.data=target_post.content

  if request.method=='POST':
    target_post.title=edit_post_form.title.data
    target_post.content=edit_post_form.content.data

    banner=request.files['banner']
    if banner:
      filename=secure_filename(banner.filename)
      banner.save(os.path.join('app/static/images',filename))
      file_path=f'images/{filename}'
      target_post.banner_path=file_path

    target_post.save_post()
    flash('update successful','success')
    return redirect(url_for('main.blog_post',id=id))

  return render_template('edit_post.html',edit_post_form=edit_post_form)



@main.route('/comment/<id>/delete')
def delete_comment(id):
  target_comment=Comment.query.filter_by(id=id).first()
  target_comment.delete_comment()
  flash('comment deleted successfully','success')
  return redirect(request.referrer)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/user/<user_name>/profile/edit',methods=['GET','POST'])
@login_required
def edit_profile(user_name):
  user=User.query.filter_by(id=current_user.id).first()
  # posts=Post.query.filter_by(user=current_user,status='active').all()
  if request.method=='POST':
    
    photo=request.files['photo']
    if photo and allowed_file(photo.filename):
      bio=request.form.get('bio')
      filename=secure_filename(photo.filename)
      photo.save(os.path.join('app/static/profile_pics',filename))
      user.profile_pic_path=f'profile_pics/{filename}'
      if bio:
        user.bio=bio
        user.save_user()
      user.save_user()
      flash('Update Successful','success')
    else:
      flash('Please provide a valid file','error')
  
  return render_template('profile/update.html',user=user)