import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import json
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
def add_dv(dv):
  app_tables.tasks.add_row(dv, complete=False)
  
@anvil.server.callable
def delete_dv(dv):
  # check that the entry being deleted exists in the Data Table
  if app_tables.dev_tbl.has_row(dv):
    dv.delete()
  else:
    raise Exception("DV does not exist")
    
@anvil.server.callable
def init_db():
  dev_list =  app_tables.dev_tbl.search()
  name_list = [r['name'] for r in dev_list]
  print(name_list)
  if (name_list == []):
    app_tables.dev_tbl.add_row(name = "CCTV-B2-10", ip = "192.168.0.10", snap_url = "http://192.168.0.10/snap/snap.jpg", updated_at=datetime.strptime("2024-08-01 00:00:00", "%Y-%m-%d %H:%M:%S"), feature_url="http://svc.parkingai.kr:23000/uploads/202408/10/region/CCTV-B2-10_20240810164523_959239-1.jpg")
    app_tables.dev_tbl.add_row(name = "CCTV-B2-11", ip = "192.168.0.11", snap_url = "http://192.168.0.11/snap/snap.jpg", updated_at = datetime.strptime("2024-08-01 00:00:00", "%Y-%m-%d %H:%M:%S"), feature_url = "http://svc.parkingai.kr:23000/uploads/202408/09/region/CCTV-B2-10_20240809200323_262735-1.jpg")
    print("empty table. added 2 rows")
  else: 
    
    print("filled table:" + json.dumps(name_list))
