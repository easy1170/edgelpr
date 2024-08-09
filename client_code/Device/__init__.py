from ._anvil_designer import DeviceTemplate
from anvil import *


class Device(DeviceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
