from django.db import models

# Create your models here.

class Loginuser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32,null=True,blank=True)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    photo = models.ImageField(upload_to='images',null=True,blank=True)
    age=models.IntegerField(null=True,blank=True,default=0)
    gender = models.CharField(max_length=4,null=True,blank=True)
    address =  models.TextField(null=True,blank=True)
    ##0是卖家 1是买家 2是管理员
    user_type = models.IntegerField(default=1)

class GoodsType(models.Model):
    type_label=models.CharField(max_length=32)
    type_description=models.TextField()
    type_picture = models.ImageField(upload_to='img')

class Goods(models.Model):
    goods_number = models.CharField(max_length=11,verbose_name='商品编号')
    goods_name = models.CharField(max_length=32,verbose_name='商品名字')
    goods_price = models.FloatField(verbose_name='商品价格')
    goods_count = models.IntegerField(verbose_name='商品数量')
    goods_location = models.CharField(max_length=254,verbose_name='商品地址')
    goods_safe_date = models.IntegerField(verbose_name='保质期')
    goods_status = models.IntegerField()  #0 表示下架 1 表示上架
    goods_pro_time = models.DateField(auto_now=True,verbose_name='生产日期')
    picture = models.ImageField(upload_to='img')
    goods_description = models.TextField(default='good,good,good....')
    # 类型 一对多
    goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE,default=1)
    # 店铺 一对多
    goods_store=models.ForeignKey(to=Loginuser,on_delete=models.CASCADE,default=1)






