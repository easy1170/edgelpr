from ._anvil_designer import PredictTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Predict(PredictTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    ret = anvil.server.call("classify_img", file)
    self.result_tb.text = ret