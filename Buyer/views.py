from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from Saller.models import *
import hashlib
import math,time
from Buyer.models import *
from alipay import AliPay
from Qshop.settings import alipay_private_key_string,alipay_public_key_string

# Create your views here.
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def LoginVaild(func):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get('name')
        session_username=request.session.get('username')
        if username and session_username and username == session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Buyer/login/')
    return inner

def index(request):
    goods_type = GoodsType.objects.all()
    result = []
    for type in goods_type:
        goods = type.goods_set.order_by('-goods_price')
        if len(goods)>4:
            goods = goods[:4]
        result.append({'type':type,'goods':goods})
    return render(request,'buyer/index.html',locals())
def login(request):
    if request.method == 'POST':
        result = ''
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            user = Loginuser.objects.filter(email=email,user_type=1).first()
            if user:
                if user.password == setPassword(password):
                    responese = HttpResponseRedirect('/Buyer/index/')
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
    return render(request,'buyer/login.html',locals())
def register(request):
    if request.method == 'POST':
        result = ''
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            loginuser = Loginuser.objects.filter(email=email).first()
            if not loginuser:
                user = Loginuser()
                user.email = email
                user.password = setPassword(password)
                user.save()
                return HttpResponseRedirect('/Buyer/login/')
            else:
                result = '邮箱已存在'
        else:
            result = '请输入邮箱'
    return render(request,'buyer/register.html',locals())

def base(request):
    return render(request,'buyer/base.html')
def loginout(request):
    response = HttpResponseRedirect('/Buyer/login/')
    keys = request.COOKIES.keys()
    for i in keys:
        response.delete_cookie(i)
    del request.session['username']
    return response

def goods_list(request):
    keywords = request.GET.get('keywords')
    req_type = request.GET.get('req_type')
    # goods_type = GoodsType.objects.get(id=keywords)
    # goods = goods_type.goods_set.all()
    # print(keywords)
    if req_type == 'findall':
        goods_type = GoodsType.objects.get(id = keywords)
        goods = goods_type.goods_set.all()
    elif req_type == 'search':
        goods = Goods.objects.filter(goods_name__contains=keywords).all()
    recommend = goods.order_by('-goods_pro_time')[:math.ceil(len(goods)/5)] #向上取整

    return render(request,'buyer/goods_list.html',locals())

@LoginVaild
def user_center_info(request):
    return render(request,'buyer/user_center_info.html',locals())


def detail(request,id):
    goods = Goods.objects.get(id=int(id))
    return render(request,'buyer/detail.html',locals())

@LoginVaild
def place_order_more(request):
    data = request.GET
    userid = request.COOKIES.get('id')
    # 区分 通过获取前端get请求的参数，找到goods_id和对应的数量
    # startswith 以goods开始的key
    data_item = data.items()
    request_data = []
    for key,value in data_item:
    # print('%s-----%s'%(key,value))   key: goods_商品id_购物车id

        if key.startswith('goods'):
            goods_id = key.split('_')[1]
            count = request.GET.get('count_'+goods_id)
            cart_id = key.split('_')[2]
            request_data.append((int(goods_id),int(count),int(cart_id)))


    if request_data:
        payorder = PayOrder()
        order_number = str(time.time()).replace('.', '')
        payorder.order_number = order_number # 订单编号
        payorder.order_status = 0
        payorder.order_total = 0
        payorder.order_user = Loginuser.objects.get(id = userid)
        order_total = 0
        total_count = 0
        payorder.save()
            # 订单详情 保存多条，一种商品一条数据
        for goods_id_one,count_one,cart_id in request_data:
            # 遍历到一条订单中的多个商品的id和对应的数量
            goods = Goods.objects.get(id=goods_id_one)
            orderinfo = OrderInfo()
            orderinfo.order_id = payorder
            orderinfo.goods = goods
            orderinfo.goods_count = count_one
            orderinfo.goods_price = goods.goods_price
            orderinfo.goods_total_price = goods.goods_price * count_one
            orderinfo.store_id = goods.goods_store
            orderinfo.save()
            order_total += goods.goods_price * count_one
            total_count += count_one
            # order_total += goods.goods_price * count_one
            # total_count += count_one

            cart = Cart.objects.get(id = cart_id)
            cart.order_number = order_number
            cart.save()


        payorder.order_total = order_total
        payorder.save()






    # # 订单数量
    #
    #
    # total_count = 0
    # all_goods_info = payorder.orderinfo_set.all()
    # for one in all_goods_info:
    # total_count += one.goods_count




    # 商品id
    # 生产订单编号





    return render(request,'buyer/place_order.html',locals())

@LoginVaild
def place_order(request):
    goods_id = request.GET.get('goods_id')    ##商品id
    goods_count = request.GET.get('goods_count')    ##商品数量
    print(goods_id,goods_count)
    user_id = request.COOKIES.get('id')
    if goods_id and goods_count:
        goods_id = int(goods_id)
        goods_count = int(goods_count)
        # user_id = int(user_id)
        # print(user_id)
        goods = Goods.objects.get(id=goods_id)
        payorder = PayOrder()
        order_number = str(time.time()).replace('.','')
        payorder.order_number = order_number
        payorder.order_status = 0
        payorder.order_total = goods.goods_price*goods_count
        payorder.order_user = Loginuser.objects.get(id=user_id)
        payorder.save()
        orderinfo = OrderInfo()
        orderinfo.order_id = payorder
        orderinfo.goods = goods
        orderinfo.goods_count = goods_count
        orderinfo.goods_total_price = goods.goods_price*goods_count
        orderinfo.store_id = goods.goods_store
        orderinfo.save()
    return render(request,'buyer/place_order.html',locals())

@LoginVaild
def Pay(request):
    order_id = request.GET.get('id')
    payorder = PayOrder.objects.get(id=order_id)
    ###实例化支付对象
    alipay = AliPay(
        appid=2016101300673952,
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
    )

    ##实例化订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject='速效生发液',  ##交易主题
        out_trade_no=payorder.order_number,  ##订单号
        total_amount=str(payorder.order_total),  ###交易总金额
        return_url='http://127.0.0.1:8000/Buyer/payresult/',  ##请求支付，之后及时回调的一个借口
        notify_url='http://127.0.0.1:8000/Buyer/payresult/',  ###通知地址，
    )

    ##    发送支付请求
    ##   请求地址  支付网关 + 实例化订单
    result = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return HttpResponseRedirect(result)
def payresult(request):
    order_number = request.GET.get('out_trade_no')
    payorder = PayOrder.objects.get(order_number=order_number)
    payorder.order_status = 1
    payorder.save()
    return render(request,'buyer/payresult.html',locals())

def add_cart(request):
    result = {'code':10000,'msg':''}
    if request.method =='POST':
        goods_id = request.POST.get('goods_id')
        count = float(request.POST.get('count',1))   ##默认值1
        user_id= request.COOKIES.get('id')
        goods = Goods.objects.get(id=goods_id)
        cart = Cart()
        cart.goods_number = count
        cart.goods_price = goods.goods_price
        cart.goods_total = goods.goods_price*count
        cart.goods = goods
        cart.cart_user = Loginuser.objects.get(id=user_id)
        cart.save()
        result['code']=10000
        result['msg']='添加成功'
    else:
        result['code']=10001
        result['msg']='添加失败'
    return JsonResponse(result)
@LoginVaild
def cart(request):
    user_id = request.COOKIES.get('id')
    cart_list = []
    cart = Cart.objects.filter(cart_user_id=user_id).order_by('-id')
    count = cart.count()  ##获取条数
    for one in cart:
        if one.order_number != '0':
            ###说明有订单号，订单状态不为已支付
            payorder =PayOrder.objects.get(order_number= one.order_number )
            if payorder.order_status != 1:
                cart_list.append(one)
            else:
                count -=1
        else:
            cart_list.append(one)
    count = cart.count()

    return render(request,'buyer/cart.html',locals())
def user_center_order(request):
    return render(request,'buyer/user_center_order.html',locals())

from CeleryTask.tasks import *
def reqtest(request):
#     ##执行celery任务
    test.delay()##发布任务  固定写法
#     # name = request.GET.get('name')
#     # age = request.GET.get('age')
#     # myprint.de
#
    return HttpResponse('sadnan')