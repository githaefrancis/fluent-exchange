import unittest
from app.models import Subscriber

class SubscriberModelTest(unittest.TestCase):
  def setUp(self):
    self.new_subscriber=Subscriber(name="John Kamau",email="johnkamau@gmail.com")


  def tearDown(self):
    Subscriber.query.delete()

  def test_variable_instances(self):
    self.assertEquals(self.new_subscriber.name,'John Kamau')
    self.assertEquals(self.new_subscriber.email,'johnkamau@gmail.com')

  def test_save_subscriber(self):
    self.new_subscriber.save_subscriber()
    self.assertTrue(len(Subscriber.query.all())>0)