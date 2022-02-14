from distutils.text_file import TextFile
from flask_wtf import FlaskForm

from wtforms import TextAreaField,SubmitField,FileField,StringField,EmailField
from wtforms.validators import InputRequired,Email


class PostForm(FlaskForm):
  title=StringField('Title',validators=[InputRequired()])
  banner=FileField('Banner image',validators=[InputRequired()])
  content=TextAreaField('',validators=[],render_kw={"placeholder": "New Post"})
  submit=SubmitField('Submit')

class CommentForm(FlaskForm):
  comment=TextAreaField('',validators=[],render_kw={"placeholder":"Comment"})
  submit=SubmitField('Submit')

class SubscribeForm(FlaskForm):
  name=StringField('',validators=[InputRequired()],render_kw={"placeholder":"name"})
  email=EmailField('',validators=[InputRequired(),Email()],render_kw={"placeholder":"email"})
  SubmitField=SubmitField('Subscribe')