import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
import anvil.media
from anvil.tables import app_tables
import anvil.server
import io
import pandas as pd
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
def export_to_excel():
     all_change_notes= app_tables.change_notes.search()
 
# For each row, pull out only the data we want to put into pandas
     dicts = [{'new_change_note_id': r['new_change_note_id'], 'title': r['title']}#, 'change_date': r['change_date']}
         for r in all_change_notes]
#'],
     df = pd.DataFrame.from_dict(dicts)
     # df = pd.DataFrame(data, columns=columns)
     content = io.BytesIO()
     df.to_excel(content, index=False)
     content.seek(0, 0)
     return anvil.BlobMedia(content=content.read(), content_type="application/vnd.ms-excel" , name = 'Change_note.xlsx')