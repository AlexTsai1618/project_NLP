import os, json
import pandas as pd
from datetime import datetime
import sqlite3 
path_to_json = '../project_NLP/bin/JSON_DATAS/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
conn = sqlite3.connect('11/db.sqlite3')
c = conn.cursor()
try:
  for index,js in enumerate(json_files):
      with open(os.path.join(path_to_json,js)) as json_file:
        json_text = json.load(json_file)
        print("loading------------")
        dgame = json_text[0]["Game"]
        c.execute("INSERT INTO ttes(game) VALUES (?);",(dgame,))
        conn.commit()
  print("success") 
	
except:
  print("No new data")
