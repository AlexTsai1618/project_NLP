from django.shortcuts import render
from .models import Music
from .models import fucker
import json
from django.http import HttpResponse
import os
import datetime

# Create your views here.
def hello_view(request):
    raw = Music.objects.filter().all()

    return render(request, 'hello_django.html', {
        'data':  raw,
    })

def index(request):
    return render(request, 'index.html', {
    })

def test(request):
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # f = open(BASE_DIR+"/jasonfiled.json", "r").read()#Ū�ɮ�
    #
    # data_set = json.loads(f);#��json�নpyhton dictionary
    #
    # obj = data_set.get('reviews')#python dictionary����
    # # for i in range(0,len(obj)):#�ڤ]���M������Ū���ܦ�list�N����for-loop�ন��dictionary
	# #     temp = dict(obj[i])#��list��^dictionary
	# #     review = temp['review']#dictionaryŪ��
	# #     voted_up = temp['voted_up']#dictionaryŪ��
    # #
    path_to_json = '../project_NLP/bin/JSON_DATAS/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # here I define my pandas Dataframe with the columns I want to get from the json
    jsons_data = pd.DataFrame(columns=['game', 'time', 'review'])  # 'country', 'city', 'long/lat'])

    # we need both the json and an index number so use enumerate()
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            # here you need to know the layout of your json and each json has to have
            # the same structure (obviously not the structure I have here)
            # game = json_text[0]["Game"]
            reviews = json_text[1]['reviews']
            len_review = len(reviews)
            for i in range(0, len(reviews)):
                review = json_text[1]['reviews'][i]['review']
                utime = json_text[1]['reviews'][i]['timestamp_updated']
                time = datetime.utcfromtimestamp(utime).strftime('%Y-%m-%d %H:%M:%S')
                game = json_text[0]['Game']

	newitem = Music(review = review ,time =  time,game = game)#Django�s��model����k�A�o�ڨS��k���A�աA�ۤv�ק�ݬݶ�
    newitem.save()
    return HttpResponse("<h1 align='center'>JSON�g�J�@�~�����I</h1><script>alert('�g�J�����I')</script>")

"""
�p�G���n������N����������url���L�a�ڳ��o�˳B�z��
"""


def print1(request):
    rrr = fucker.objects.filter().all()


    return render(request, 'print1.html', {
        'ddd': rrr,
    }