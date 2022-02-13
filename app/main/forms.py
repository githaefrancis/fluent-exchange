from flask_wtf import FlaskForm

from wtforms import TextAreaField,SubmitField,FileField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
  banner=FileField('Banner image',validators=[InputRequired()])
  content=TextAreaField('',validators=[InputRequired()],render_kw={"placeholder": "New Post"})
  submit=SubmitField('Submit')