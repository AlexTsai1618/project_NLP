import os
import sqlite3
path, _ = os.path.split(os.path.realpath(__file__))
conn = sqlite3.connect('./11/db.sqlite3')
conneted_sqlite = conn.cursor()
raw = conneted_sqlite.execute('select * from music')
temp = list(raw)

for i in range(0,len(temp)):
  id_temp = temp[i][0]
  raw = temp[i][3]
  raw = raw.split(' ')
  raw = raw[0]
  raw = raw.split('-')
  year = raw[0]
  month = raw[1]
  #yearmonth=raw[0]+('-')+raw[1]
  day = raw[2]
  #conneted_sqlite.execute('update music set yearmonth="{}",  day="{}" where\
  #id="{}"'.format(yearmonth,day,id_temp))
  conneted_sqlite.execute('update music set year="{}", month="{}", day="{}" where\
    	id="{}"'.format(year,month,day,id_temp))
  conn.commit()
  print(i+1,'/',len(temp))
conn.close()
