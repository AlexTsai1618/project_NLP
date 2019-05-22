import sqlite3 as s
import re
conn = s.connect('testDB.db')
cursor = conn.cursor()
d = cursor.execute('SELECT review from music')
a = {}
for i in d:
   i.replace('\','')
   i.replace('(','')
   i.replace(')','')
   a = i
   print(a)
