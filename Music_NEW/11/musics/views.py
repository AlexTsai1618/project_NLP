from django.shortcuts import render,render_to_response
from .models import Music
import json
from django.http import HttpResponse
import os
import datetime
import sqlite3
import jieba.posseg as pseg
import os
import sys
import json
import requests
import sqlite3
import jieba.analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
def hello_view(request):
    raw = Music.objects.filter().all()

    return render(request, 'hello_django.html', {
        'data':  raw,
    })

def index(request):
    return render(request, 'index.html', {
    })
def search_form(request):
   return render_to_response('search_form.html')
def test(request):
    path_to_json = '../project_NLP/bin/JSON_DATAS/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    conn=sqlite3.connect('../db.sqlite3')
    c=conn.cursor
    jsons_data = pd.DataFrame(columns=['game', 'time', 'review'])  # 'country', 'city', 'long/lat'])
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            # here you need to know the layout of your json and each json has to have
            # the same structure (obviously not the structure I have here)
            # game = json_text[0]["Game"]
            reviews = json_text[1]['reviews']
            len_review = len(reviews)
            for i in range(0, len(reviews)):
                dreview = json_text[1]['reviews'][i]['review']
                utime = json_text[1]['reviews'][i]['timestamp_updated']
                dtime = datetime.utcfromtimestamp(utime).strftime('%Y-%m-%d %H:%M:%S')
                dgame = json_text[0]['Game']
                
                c.execute("INSERT INTO music(game,time,review) VALUES(?,?,?);" (dgame,dtime,dreview))
                #newitem = Music(review = review ,time = time,game = game)
                #newitem.save()
                conn.commit()
                jsons_data.loc[index]=['game','time','review']
    
    
    return HttpResponse("<h1 align='center'>JSON Done</h1><script>alert('Done')</script>")

def print1(request):
    rrr = Music.objects.filter().all()


    return render(request, 'print1.html', {
        'ddd': rrr,
    })
def proportion1(request):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    game_name=[]
    cursor1 = c.execute("SELECT game FROM music ")
    raw=list(cursor1)

    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])


    return render(request, 'proportion1.html', {
          'game_name':game_name,
    })
def search_donut(request):
    conn = sqlite3.connect('db.sqlite3')
    c2 = conn.cursor()
    game_name=[]
    cursor12 = c2.execute("SELECT game FROM npsave ")
    raw=list(cursor12)

    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])
    
    c = conn.cursor()

    request.encoding = 'utf-8'
    if 'q' in request.GET:
        game = request.GET['q']
        cursor = c.execute("SELECT positive,negative,game FROM npsave where game = ?",(game,))
    else:
        game = 'Null'
    raw = list(cursor)
    positive = raw[0][0]
    negative = raw[0][1]
    for i in range(0,len(raw)):
        if not raw[i][2] in game_name:
           game_name.append(raw[i][2])
    return render(request, 'proportion1.html', {
        #'data':  raw,
        'game_name':game_name,
        'positive':positive,
        'negative':negative,
        'game':game,
    })
    
def count_date(request):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    game_name=[]
    cursor1 = c.execute("SELECT game FROM npsave ")
    raw=list(cursor1)

    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])

    return render(request,'count_date.html',{
    'game_name':game_name,
    })    
def search_date(request):
    conn1 = sqlite3.connect('db.sqlite3')
    conneted_sqlite = conn1.cursor()
    game_name=[]
    cursor1 = conneted_sqlite.execute("SELECT game FROM npsave ")
    raw=list(cursor1)

    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])





     
    if 'q' in request.GET:
        game = request.GET['q']
        
    else:
        game = 'nullll'    
    raw1 = conneted_sqlite.execute('select id, year, month from music where game = ?',(game,))
    raw1 = list(raw1)
    temp = {}
    for i in range(0,len(raw1)):
      if len(str(raw1[i][2]))==1:
           month = '-0'+str(raw1[i][2])
      else:
           month ='-'+str(raw1[i][2])
      time = str(raw1[i][1])+str(month)
	    
      if time in temp:
			    temp[time] = temp[time]+1
      else:
			    temp[time] = 1

    return render(request, 'count_date.html',{
        'temp':temp,
        'game_name':game_name,'game':game,})
def search_text_cloud(request):




    conn1 = sqlite3.connect('db.sqlite3')
    conneted_sqlite = conn1.cursor()
    game_name=[]
    cursor1 = conneted_sqlite.execute("SELECT game FROM npsave ")
    raw=list(cursor1)

    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])





    conn3 = sqlite3.connect('/home/alextsai0429/Music/11/db.sqlite3')
    c2 = conn3.cursor()
    textcloud = {}
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        game = request.GET['q']
    else:
        game = 'Null'
    cursor2 = c2.execute("SELECT id,review FROM music WHERE review IS NOT NULL AND game = ?",(game,))
    for id,review in cursor2.fetchall(): 
        keywords = jieba.analyse.extract_tags(review, topK=20, withWeight=True, allowPOS=('n','nr','ns')) 
        for item in keywords:
           textcloud[item[0]]= item[1]

    return render(request,'text_cloud.html',{
    'textcloud':textcloud,'game_name':game_name,'game':game,
    })
def text_cloud(request):
    conn4 = sqlite3.connect('db.sqlite3')
    c4 = conn4.cursor()
    game_name=[]
    cursor4 = c4.execute("SELECT game FROM npsave ")
    raw=list(cursor4)
    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])
    return render(request,'text_cloud.html',{
    'game_name':game_name})
def youtube(request):
    conn4 = sqlite3.connect('db.sqlite3')
    c4 = conn4.cursor()
    game_name=[]
    cursor4 = c4.execute("SELECT game FROM npsave ")
    raw=list(cursor4)
    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])
    return render(request,'youtube.html',{
    'game_name':game_name})
def youtube_search(request):
    #import urllib2
    #import requests
    #import json
    conn4 = sqlite3.connect('db.sqlite3')
    c4 = conn4.cursor()
    game_name=[]
    cursor4 = c4.execute("SELECT game FROM npsave ")
    raw=list(cursor4)
    for i in range(0,len(raw)):
        if not raw[i][0] in game_name:
           game_name.append(raw[i][0])
    key = 'AIzaSyAlUhCMmr0abMMNV1JccNV0_rLXWZG0bnU'
    if 'q' in request.GET:
        game = request.GET['q']
    else:
        game = 'Null'

    if 'b' in request.GET:
        num = request.GET['b']
    else:
        num = 'Null'        
    
    r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults="+num+"&order=viewCount&q="+game+"&type=video&videoEmbeddable=true&key="+key)
    a = r.json()
    video_id=[]
    for i in range(0,int(num)):
       video_id.append(a['items'][i]['id']['videoId']) 
    return render(request,'youtube.html',{'game':game,'video_id':video_id,'game_name':game_name})
