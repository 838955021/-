# Generated by Django 2.2.1 on 2019-09-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0004_auto_20190924_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodstype',
            name='type_picture',
            field=models.ImageField(default='img/1.png', upload_to='img'),
            preserve_default=False,
        ),
    ]
