import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from anvil import open_form, alert
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



def say_hello():
  print("Hello, world")
def main():
  say_hello()
  anvil.server.call('init_db')
  #anvil.server.call('intervalFunc')
  #anvil.server.call('startWebsocket')
  open_form('Base')
  
  
if __name__ == '__main__':
  main()