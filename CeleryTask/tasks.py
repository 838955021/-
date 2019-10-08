from __future__ import absolute_import
from Qshop.celery import app
import time

##创建任务
@app.task     ##将普通函数转换成selery 任务
def test():
    print('----i am test task----')
    return 'i am test task'

@app.task
def myprint(name,age):
    time.sleep(5)
    print("%s:%s"%(name,age))
    return 'woshi myprint'

@app.task
def send_email(params):
    ##  发送邮件的代码
    return 'send email'