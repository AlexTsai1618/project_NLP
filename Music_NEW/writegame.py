import os
import sqlite3
path, _ = os.path.split(os.path.realpath(__file__))
conn = sqlite3.connect(path+'/11/db.sqlite3')
conneted_sqlite = conn.cursor()
#raw = conneted_sqlite.execute('select game, aview from music')
raw = conneted_sqlite.execute('select game, aview from music where aview!="none"')
game_name = {}

raw = list(raw)
print(len(raw))
for i in range(0,len(raw)):
	#print(raw[i][0])
	if raw[i][0] in game_name:
		if raw[i][1]=='positive':

			pos = int(game_name[raw[i][0]][1])+1
			game_name[raw[i][0]][1]=pos
		else:
			neg = int(game_name[raw[i][0]][2])+1
			game_name[raw[i][0]][2]=neg
		num = int(game_name[raw[i][0]][0])+1
		game_name[raw[i][0]][0] = num

	else:

		if raw[i][1]=='positive':

			game_name[raw[i][0]] = [1,0,0]
			pos = int(game_name[raw[i][0]][1])+1
			game_name[raw[i][0]][1]=pos
			

		else:

			game_name[raw[i][0]] = [1,0,0]
			neg = int(game_name[raw[i][0]][2])+1
			game_name[raw[i][0]][2]=neg
for key,value in game_name.items():
  print(key,"total reviews:",value[0],"pos",value[1],"neg:",value[2])
  conneted_sqlite.execute("INSERT INTO ttes(game) VALUES (?);",(key,))
  #conneted_sqlite.execute('update npsave set positive="{}", negative="{}"where\
      #game="{}"'.format(value[1],value[2],key))
  #conneted_sqlite.execute('update ttes set positive="{}", negative="{}"where\
      #game="{}"'.format(value[1],value[2],key))
  conn.commit()
conn.close()
#print(game_name)

#for key, value in game_name.items():

	#print(key,"total reviews:",value[0],"Pos:",value[1],"Neg:",value[2])
  
  
  
  #conn.commit()
#conn.close()
  
	