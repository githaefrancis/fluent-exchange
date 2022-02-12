import unittest

from app.models import User,Role,Post,Comment

class CommentModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis Githae",username='fgithae',password='password',email="francis@gmail.com",role=Role.query.filter_by(id=1).first())
    self.new_post=Post(user=self.new_user,title="The beginning",content="This is the first post ever in this channel.The fluent debutter",banner_path="images/img1.jpg")
    self.new_comment=Comment(user=self.new_user,post=self.new_post,content="It's actually good")

  def tearDown(self):
    Comment.query.delete()
    Post.query.delete()
    User.query.delete()

  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.user,self.new_user)
    self.assertEquals(self.new_comment.post,self.new_post)
    self.assertEquals(self.new_comment.content,"It's actually good")
    
  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all())>0)

  def test_delete_comment(self):
    self.new_comment.delete_comment()
    self.assertEquals(self.new_comment.status,'archived')
  