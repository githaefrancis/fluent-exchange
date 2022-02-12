from datetime import datetime

from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from . import db

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
  ''''
  Class that defines the user model
  '''
  __tablename__='users'
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(255))
  username=db.Column(db.String(255))
  email=db.Column(db.String(255))
  created_at=db.Column(db.DateTime,default=datetime.utcnow)
  bio=db.Column(db.String(255))
  profile_pic_path=db.Column(db.String(255))
  password_secure=db.Column(db.String(255))
  role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
  posts=db.relationship('Post',backref='user',lazy='dynamic')
  comments=db.relationship('Comment',backref='user',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  

  @password.setter
  def password(self,password):
    self.password_secure=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password,password)

  def __repr__(self):
    return f'User{self.username}'


class Role(db.Model):
  '''
  Role class to define user roles
  
  '''
  __tablename__='roles'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  users=db.relationship('User',backref='role',lazy='dynamic')


class Post(db.Model):
  '''
  class to define post model
  '''
  __tablename__='posts'
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(255))
  content=db.Column(db.Text)
  banner_path=db.Column(db.String(255))
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
  comments=db.relationship('Comment',backref='post',lazy='dynamic')
  status=db.Column(db.String(255),default='active')
  created_at=db.Column(db.DateTime,default=datetime.utcnow)


class Comment(db.Model):
  '''
  class to define the comment model

  '''
  __tablename__='comments'
  id=db.Column(db.Integer,primary_key=True)
  content=db.Column(db.String(500))
  created_at=db.Column(db.DateTime,default=datetime.utcnow)
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
  post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))
  status=db.Column(db.String(255))

class Subscriber(db.Model):
  '''
  class to define the subscriber model
  '''

  __tablename__='subscribers'
  id=db.Column(db.Integer,primary_key=True)
  email=db.Column(db.String(255))
  created_at=db.Column(db.DateTime,default=datetime.utcnow)
  active=db.Column(db.Boolean,default=True)

class Quote:
  '''
  class to define the structure of the Quoute
  '''
  def __init__(self,quote_id,author,content,link):
    self.quote_id=quote_id
    self.author=author
    self.content=content
    self.link=link

  # def __repr__(self):
  #   return self.content



