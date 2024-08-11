import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_dv_list():
  return app_tables.dev_tbl.search()
  
@anvil.server.route("/dv/list")
def get_user_list():
  return app_tables.dev_tbl.search()
  
@anvil.server.callable
def update_dv(dv, dv_dict):
  # check that the entry given is really a row in the ‘entries’ table
  print(dv_dict)
  if app_tables.dev_tbl.has_row(dv):
    dv_dict['updated_at'] = datetime.now()
    dv.update(**dv_dict)
    print(dv_dict)
  else:
    raise Exception("DV does not exist")

@anvil.server.callable
def delete_dv(dv):
  # check that the entry being deleted exists in the Data Table
  if app_tables.dev_tbl.has_row(dv):
    dv.delete()
  else:
    raise Exception("DV does not exist")