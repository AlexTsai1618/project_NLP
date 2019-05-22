import os
import sqlite3
path, _ = os.path.split(os.path.realpath(__file__))
conn = sqlite3.connect(path+'/11/db.sqlite3')
conneted_sqlite = conn.cursor()
#raw = conneted_sqlite.execute('select game, aview from music')
raw = conneted_sqlite.execute('select game, id, year, month from music where aview!="none"')
game_name = {}


raw = list(raw)
print(len(raw))
temp = {}
for i in range(0,len(raw)):
	if len(str(raw[i][3]))==1:
		month = '-0'+str(raw[i][3])
	else:
		month = '-'+str(raw[i][3])
	time = str(raw[i][2])+str(month)
	if raw[i][0] in temp:
		if time in temp[raw[i][0]]:
			temp[raw[i][0]][time] = str(temp[raw[i][0]][time]) + ','+str(raw[i][1])
		else:
			temp[raw[i][0]][time] = str(raw[i][1])
	else:
		temp[raw[i][0]]={}
		if time in temp[raw[i][0]]:
			temp[raw[i][0]][time] = str(temp[raw[0]][time]) + ','+str(raw[i][1])
		else:
			temp[raw[i][0]][time] = str(raw[i][1])
#print(temp)
total=0
for key, value in temp.items():
	for month, ids in value.items():
		ids = ids.split(',')
		length = len(ids)
		total = total + length
		print("game",key,"month",month,"comment",(length),'id',ids)
#assert total == len(raw)