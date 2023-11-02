import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
import anvil.media
from anvil.tables import app_tables
import anvil.server
import anvil.tz
import io
import pandas as pd
from datetime import datetime, time , date , timedelta, timezone

@anvil.server.callable
def export_to_csv():
  """Launch a single crawler background task."""
  task = anvil.server.launch_background_task('make_backup')
  
  
@anvil.server.background_task
@anvil.server.callable
def make_backup():
     change_note_csv = app_tables.change_notes.search().to_csv()
     change_note_audit_csv = app_tables.change_notes_audit.search().to_csv()
     users_csv = app_tables.users.search().to_csv()
     change_id_counter_csv = app_tables.change_id_counter.search().to_csv()
     supported_products_csv = app_tables.suppported_products.search().to_csv()
  
     today = datetime.now() 
  
     folder = app_files.change_note_system_tables_backup
     new_folder = folder.create_folder('change_note_backup'+'_'+str(today))
     filename0 = 'change_note' + '_' +str(today)+' .csv'
     filename1 = 'change_note_audit' + '_' +str(today)+' .csv'
     filename2 = 'users' + '_' +str(today)+' .csv'
     filename3 = 'change_id_counter' + '_' +str(today)+' .csv'
     filename4 = 'supported_products' + '_' +str(today)+' .csv'
     new_file0 = new_folder.create_file(filename0, change_note_csv)
     new_file1 = new_folder.create_file(filename1, change_note_audit_csv )
     new_file2 = new_folder.create_file(filename2, users_csv)
     new_file3 = new_folder.create_file(filename3, change_id_counter_csv)
     new_file4 = new_folder.create_file(filename4, supported_products_csv)
     address ='syd'
     send_email(address)




  
     # return change_note_csv, change_note_audit_csv, users_csv, change_id_counter_csv, supported_products_csv

@anvil.server.callable
def send_email(address):
    anvil.email.send(
                 from_name = "Change Note Backup", 
                 to = "sydney.w.stewart@gmail.com",
                 subject = 'Change Note Backup Run',
                 text = "Change Note Backup Run!")