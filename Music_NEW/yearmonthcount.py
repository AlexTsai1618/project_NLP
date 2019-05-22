import os
import sqlite3
path, _ = os.path.split(os.path.realpath(__file__))
conn = sqlite3.connect(path+'/11/db.sqlite3')
c = conn.cursor()
raw = c.execute("SELECT game,yearmonth  FROM music ")
game_name = {}
ym={}
name={}
count=0
raw=list(raw)
for i in range(0,len(raw)):
  #print(raw[i][0],raw[i][1],len(raw[i][0]))
  if raw[i][0] in name:
    if raw[i][1] in ym:
      num = int(game_name[i][0])+1
      game_name[i][0]=num
    else:
      game_name[i] = [1,raw[i][1],raw[i][0]]
      ym[count1]=raw[i][1]
      count1+=1
  else:
    ym.clear()
    count1=0
    game_name[i] = [1,raw[i][1],raw[i][0]]
    ym[0]=raw[i][1]
    name[count]=raw[i][0]
    count+=1
for key,value in game_name.items():
  print(value[2],"total num:",value[0],"yearmonth",value[1])
    
