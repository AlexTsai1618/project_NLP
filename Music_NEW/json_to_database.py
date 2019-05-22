import os, json
import pandas as pd
from datetime import datetime
import sqlite3 
path_to_json = '../project_NLP/bin/JSON_DATAS/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
conn = sqlite3.connect('./11/db.sqlite3')
c = conn.cursor()
b= conn.cursor()
d = conn.cursor()
for index,js in enumerate(json_files):
    with open(os.path.join(path_to_json,js)) as json_file:
      json_text = json.load(json_file)
      reviews = json_text[1]['reviews']
      len_review=len(reviews)
      for i in range(0,len(reviews)):
            dreview = json_text[1]['reviews'][i]['review']
            utime = json_text[1]['reviews'][i]['timestamp_updated']
            dtime = datetime.utcfromtimestamp(utime).strftime('%Y-%m-%d %H:%M:%S')
            dgame = json_text[0]['Game']
            aview = ""
            #print(str(dtime)+dgame+dreview)
            c.execute("INSERT INTO music (game,time,review,aview) VALUES (?,?,?,?);",(dgame,dtime,dreview,aview))
    print('loading data :'+str(index)+'/'+str(len(json_files)))
b.execute("DELETE FROM music WHERE review ='';")#it delete all review which are NULL
d.execute("delete from music where id not in(select min(id) from music group by review)")##if duplicate datas generate it delete all ones
conn.commit()
print('finish')
