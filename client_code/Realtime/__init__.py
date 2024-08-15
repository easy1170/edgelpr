from ._anvil_designer import RealtimeTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js

#from anvil.js.window import Foo
import anvil.js.window

class Realtime(RealtimeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.items= anvil.server.call("get_dv_list")
    self.cam_drop_down.items =  [(row["name"], row) for row in self.items]
    self.dom = anvil.js.get_dom_node(self.video_container)
    self.add_event_handler('x-foo', self.handle_foo)
    
  def form_show(self, **event_args):
    from anvil.js.window import jpegView
    #print(dir(anvil.js.window))
    self.jpegView = jpegView.drawPlayer(self.dom, "/cam1/jpg/")
    print("start jpegView")
    pass
  
  def handle_foo(self, **event_args):
    name="fdsfds"
    alert(f"Hello, {name}")
    print("The x-foo event was raised!")
    
    # Any code you write here will run before the form opens.
  def canvas_jpg_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
  
    c = self.canvas_1
  
    # Get the image as a Media object
    image_media = anvil.URLMedia('https://localsegye.co.kr/news/data/20190220/p1065591123683055_345_thum.jpg')
  
    # Draw the image at position (100,100)
    c.draw_image(image_media, 100, 100)
  
    # Draw a 100x100 patch from this image,
    # Starting at pixel (50, 50) on the image,
    # at position (25, 25) on the canvas,
    # at half scale (50x50)
    c.draw_image_part(image_media,
                      50, 50, 100, 100,
                      25, 25, 50, 50)

  def interval_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().call_js('startInterval')
    #self.call_js('showJsAlert', 'Hello, world!')

