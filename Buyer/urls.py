from Buyer.views import *
from django.urls import path,re_path

urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('base/',base),
    path('loginout/',loginout),
    path('goods_list/',goods_list),
    path('user_center_info/',user_center_info),
    re_path('detail/(?P<id>\d+)',detail),
    path('place_order_more/',place_order_more),
    path('place_order/',place_order),
    path('pay/',Pay),
    path('cart/',cart),
    path('add_cart/',add_cart),
    path('payresult/',payresult),
    path('reqtest/',reqtest),
    path('user_center_order/',user_center_order),
]