from ._anvil_designer import DvEditDialogTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class DvEditDialog(DvEditDialogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  def __del__(self):
    print("unload Dialog")
    print(self.item)
    

  def edit_confirm_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
