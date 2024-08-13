from ._anvil_designer import DeviceTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..DvEditDialog import DvEditDialog


class Device(DeviceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.dv_rplist_panel.items=anvil.server.call('get_dv_list')
    self.refresh_dvList()
  #+--------------------------------------   
  def refresh_dvList(self):
    #self.dv_rplist_panel.items=app_tables.dev_tbl.search()
    self.dv_rplist_panel.items = anvil.server.call('get_dv_list')
  #+--------------------------------------
  def add_dv_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_entry = {}
    # Open an alert displaying the 'EntryEdit' Form
    save_clicked = alert(
      content=DvEditDialog(item=new_entry),
      title="Add Entry",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      anvil.server.call('add_dv', new_entry)
      self.refresh_dvList()
  #+--------------------------------------
  def delete_dv(self, entry, **event_args):
    # Delete the entry
    anvil.server.call('delete_entry', entry)
    # Refresh entry to remove the deleted entry from the Homepage
    self.refresh_entries()