# Generated by Django 2.2.1 on 2019-09-27 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0006_goods_goods_description'),
        ('Buyer', '0002_auto_20190925_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_number', models.IntegerField(verbose_name='商品数量')),
                ('goods_price', models.CharField(max_length=32, verbose_name='商品单价')),
                ('goods_total', models.CharField(max_length=32, verbose_name='总价')),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saller.Loginuser')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saller.Goods')),
            ],
        ),
    ]
