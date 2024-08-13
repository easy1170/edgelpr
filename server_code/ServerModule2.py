import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import threading
from datetime import datetime

@anvil.server.background_task
def make_slow_request():
  print("make_slow_request")
  #response = anvil.http.request("https://httpstat.us/200?sleep=1000")  # An API that provides slow responses
  #print(response)

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
def i_wanna_interval():
    print(datetime.now(), "Hi")
  
@anvil.server.callable
def intervalFunc():
  print("intervalFunc")
  set_interval(i_wanna_interval, 10)