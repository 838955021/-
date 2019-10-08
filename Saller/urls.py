from django.urls import path,re_path
from Saller.views import *

urlpatterns = [
    path('register/',register),
    path('login/',login),
    path('index/',index),
    path('loginout/',loginout),
    path('goods_list/',goods_list),
    path('personal_info/',personal_info),
    re_path('goods_list/(?P<status>[01])/(?P<page>\d+)',goods_list),
    re_path('goods_status/(?P<status>\w+)/(?P<id>\d+)',goods_status),
    path('goods_add/',goods_add),
]