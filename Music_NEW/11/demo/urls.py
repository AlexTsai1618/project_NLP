from django.conf.urls import url
from django.contrib import admin
from musics.views import hello_view, test, index,print1,proportion1,text_cloud,count_date,search_donut,search_date,text_cloud,search_text_cloud,youtube,youtube_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello_view),
    url(r'^test/', test),
    url(r'^print1/', print1),
    url(r'^index/',index),
    url(r'^proportion1$', proportion1),
    url(r'^search_donut$',search_donut),
    url(r'^text_cloud$', text_cloud),
    url(r'^count_date$', count_date),
    url(r'^search_date$', search_date),
    url(r'^text_cloud$', text_cloud),
    url(r'^search_text_cloud$', search_text_cloud),
    url(r'^youtube$', youtube),
    url(r'^youtube_search$', youtube_search),
]
