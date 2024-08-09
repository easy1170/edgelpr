from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home
from ..Realtime import Realtime

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())
    # Any code you write here will run before the form opens.

  def home_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def real_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Realtime())
