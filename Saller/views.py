from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from Saller.models import *
from django.core.paginator import Paginator
import hashlib
# Create your views here.

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def register(request):
    if request.method=='POST':
        result=''
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email :
            loginuser = Loginuser.objects.filter(email=email).first()
            if not loginuser  :
                user= Loginuser()
                user.email = email
                user.password = setPassword(password)
                user.save()
                return HttpResponseRedirect('/Saller/login/')
            else:
                result = '邮箱已存在'
        else:
            result = '请输入邮箱'
    return render(request,'saller/register.html',locals())

def login(request):
    if request.method == 'POST':
        result = ''
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            user = Loginuser.objects.filter(email=email,user_type=0).first()
            if user:
                if user.password == setPassword(password):
                    responese = HttpResponseRedirect('/Saller/index/')
                    responese.set_cookie('name',user.email)
                    responese.set_cookie('id',user.id)
                    request.session['username']=user.email
                    return responese
                else:
                    result='密码错误请重新输入'
            else:
                result='用户不存在'
        else:
            result = '请输入邮箱'
    return render(request,'saller/login.html',locals())

def LoginVaild(func):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get('name')
        session_username=request.session.get('username')
        if username and session_username and username == session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Saller/login/')
    return inner

@LoginVaild
def index(request):
    return render(request, 'saller/index.html')

def loginout(request):
    response = HttpResponseRedirect('/Saller/login/')
    keys = request.COOKIES.keys()
    for i in keys:
        response.delete_cookie(i)
    del request.session['username']
    return response

def goods_list(request,status,page=1):
    page = int(page)
    if status == '1':
        goods_obj = Goods.objects.filter(goods_status=1).order_by('goods_number')
    else:
        goods_obj = Goods.objects.filter(goods_status=0).order_by('goods_number')
    goods_all = Paginator(goods_obj,10)
    goods_list = goods_all.page(page)
    for i in goods_list:
        print(i.goods_name)
    return render(request,'saller/goods_list.html',locals())

@LoginVaild
def personal_info(request):
    user_id = request.COOKIES.get('id')
    # print(user_id)
    user = Loginuser.objects.filter(id=user_id).first()
    if request.method == 'POST':
        data = request.POST
        user.username = data.get('username')
        user.phone_number = data.get('phone_number')
        if  data.get('age') == '':
            user.age =0
        else:
            user.age=data.get('age')
        user.gender = data.get('gender')
        user.address = data.get('address')
        if request.FILES.get('photo'):
            user.photo = request.FILES.get('photo')
        user.save()
    return render(request,'saller/personal_info.html',locals())

def goods_status(request,status,id):
    goods = Goods.objects.get(id=id)
    if status == 'up':
        goods.goods_status=1
    else:
        goods.goods_status=0
    goods.save()
    ##获取请求来源
    url = request.META.get("HTTP_REFERER","/Saller/goods_list/1/1")
    # return render(request,'goods_list.html',locals())
    return HttpResponseRedirect(url)

def goods_add(request):
    goods_type = GoodsType.objects.all()
    if request.method == 'POST':
        data = request.POST
        print(data)
        goods = Goods()
        goods.goods_number = data.get('goods_number')
        goods.goods_name = data.get('goods_name')
        goods.goods_price = data.get('goods_price')
        goods.goods_count = data.get('goods_count')
        goods.goods_location = data.get('goods_location')
        goods.goods_safe_date = data.get('goods_safe_date')
        goods.goods_status = 1
        goods_type = request.POST.get('goods_type')
        goods.goods_type = GoodsType.objects.get(id = goods_type)
        user_id = request.COOKIES.get('id')
        goods.goods_store = Loginuser.objects.get(id = user_id)
        goods.save()

    return render(request,'saller/goods_add.html',locals())