from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Realtime import Realtime
from ..Device import Device
from ..Predict import Predict
class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())
    self.user_email = None
    self.updateLoginStatus()
    # Any code you write here will run before the form opens.

  def home_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def real_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Realtime())

  def device_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Device())
  def ai_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Predict())
    
  def user_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    if (self.user_email  is not None):
      result = alert(content="로그아웃 할까요?",
               title="Logout choice",
               large=False,
               buttons=[
                 ("Yes", "YES"),
                 ("No", "NO")
               ])

      print(f"The user chose {result}")
      if result == "YES":
        anvil.users.logout()
        self.login_name.text = "SignIn"
        self.user_email = None
        return
    anvil.users.login_with_form()
    self.updateLoginStatus()
    

  def updateLoginStatus(self):
    self.user_email = None if (anvil.users.get_user() is None) else anvil.users.get_user()['email'] 
    if  self.user_email is None:
      self.login_name.text = 'SignIn'
    else:
      self.login_name.text =  self.user_email 


    