from ._anvil_designer import DvItemTemplateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...DvEditDialog import DvEditDialog

class DvItemTemplate(DvItemTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def dv_update_button_click(self, **event_args):
    dv_copy = dict(self.item)
    save_clicked = alert(
      content=DvEditDialog(item=dv_copy),
      title="장치 정보 수정하기",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    
    if save_clicked:
      anvil.server.call('update_dv', self.item, dv_copy)
  
      # Now refresh the page
      self.refresh_data_bindings()
    #row = app_tables.dev_tbl.get_by_id(event_args.)

  def dv_del_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Get the user to confirm if they wish to delete the entry
    # If yes, raise the 'x-delete-entry' event on the parent 
    # (which is the entries_panel on Homepage)
    if confirm(f"삭제를 진행할까요? {self.item['title']}?"):
      self.parent.raise_event('x-delete-entry', entry=self.item)