from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.media
import anvil.tables as tables
import anvil.tables.query as q
from anvil.google.drive import app_files
from anvil.tables import app_tables
import anvil.google.drive
from datetime import datetime, time , date , timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    today = datetime.now() 
    result = anvil.server.call("export_to_excel") #, <pa 

    folder = app_files.change_notes
    filename = 'change_note' + str(today)
    new_file = folder.create_file(filename, result)
+

