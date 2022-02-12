import unittest
from app.models import Role,User,Post

class PostModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis Githae",username='fgithae',password='password',email="francis@gmail.com",role=Role.query.filter_by(id=1).first())
    self.new_post=Post(user=self.new_user,title="The beginning",content="This is the first post ever in this channel.The fluent debutter",banner_path="images/img1.jpg")
  
  def tearDown(self):
    Post.query.delete()
    User.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_post.user,self.new_user)
    self.assertEquals(self.new_post.title,"The beginning")
    self.assertEquals(self.new_post.content,"This is the first post ever in this channel.The fluent debutter")
    self.assertEquals(self.new_post.banner_path,"images/img1.jpg")

  def test_post_save(self):
    self.new_post.save_post()
    self.assertTrue(len(Post.query.all())==1)