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

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def create_excel():
 
  print(df)
  change_note_excel = df.to_excel('change_note_excel.xlsx')
  # print(change_note_excel)


@anvil.server.callable
def export_to_csv():
     # all_change_notes= app_tables.change_notes.search()
     # all_change_note_audits =app_tables.change_notes_audit.search()
     
  
     change_note_csv = app_tables.change_notes.search().to_csv()
     change_note_audit_csv = app_tables.change_notes_audit.search().to_csv()
     users_csv = app_tables.users.search().to_csv()
     return change_note_csv, change_note_audit_csv, users_csv
     # dicts = [{'new_change_note_id': r['new_change_note_id'], 
     #           'title': r['title'],
     #           'change_date': r['change_date'].replace(tzinfo=None)}       #datetimeObject = datetimeObject.replace(tzinfo=None)
     #     for r in all_change_notes]
   
     # df = pd.DataFrame.from_dict(dicts)
     # # df = pd.DataFrame(data, columns=columns)
     # content = io.BytesIO()
     # df.to_excel(content, index=False)
     # content.seek(0, 0)
     # return anvil.BlobMedia(content=content.read(), content_type="application/vnd.ms-excel" , name = 'Change_note.xlsx')