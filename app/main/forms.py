from flask_wtf import FlaskForm

from wtforms import TextAreaField,SubmitField,FileField,StringField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
  title=StringField('Title',validators=[InputRequired()])
  banner=FileField('Banner image',validators=[InputRequired()])
  content=TextAreaField('',validators=[],render_kw={"placeholder": "New Post"})
  submit=SubmitField('Submit')