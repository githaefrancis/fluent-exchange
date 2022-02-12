import unittest

from app.models import User,Role

class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis Githae",username='fgithae',password='password',email="francis@gmail.com",role=Role.query.filter_by(id=1).first())

  def tearDown(self):
    User.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_user.role,Role.query.filter_by(id=1).first())
    self.assertEquals(self.new_user.role_id,1)
    self.assertEquals(self.new_user.name,'Francis Githae')
    self.assertEquals(self.new_user.username,'fgithae')
    self.assertEquals(self.new_user.email,'francis@gmail.com')

  def test_password_setter(self):
    self.assertTrue(self.new_user.password_secure is not None)
    

  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password  

  def test_password_verfication(self):
    self.assertTrue(self.new_user.verify_password('password'))

  def test_save_user(self):
    self.new_user.save_user()
    self.assertTrue(len(User.query.all())==1)