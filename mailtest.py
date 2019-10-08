# import smtplib
# from email.mime.text import MIMEText
# ##构建邮件
# ##主题
# subject = "0715测试demo"
# ##发送内容
# content = "you see see you day day is big pig pig"
#
# ##发送人
# sender = 'huang838955021@163.com'
# ##接收人 单个 多个
# rec = """
# 838955021@qq.com,
# """
# password = 'hjh520'
#
# ##MIMEText  参数发送内容 ， 内容类型，编码
# message = MIMEText(content,'plain','utf-8')
# message['Subject'] = subject
# message["From"] = sender ##发件人
# message['To'] = rec   #收件人
#
# ##发送邮件
# smtp = smtplib.SMTP_SSL("smtp.163.com",465)
# smtp.login(sender,password)
#
# ##参数说明     发件人    收件人需要一个列表    发送邮件   类似一种json的格式
# smtp.sendmail(sender,rec.split(",\n"),message.as_string())
# smtp.close()


import smtplib
from email.mime.text import MIMEText

###构建邮件
##主题
while True:
    subject = '我是你爸爸'

    ##内容
    content = '请叫我爸爸'

    ##发件人
    sender = '838955021@qq.com'

    ##收件人
    rec = """
    1162347614@qq.com
    """

    password = 'owkulnjykeilbdic'

    # ##MIMEText  参数发送内容 ， 内容类型，编码
    message = MIMEText(content,'plain','utf-8')
    message['Subject']=subject
    message['From']=sender
    message['To']=rec

    # ##发送邮件
    smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtp.login(sender,password)

    ### ##参数说明     发件人    收件人需要一个列表    发送邮件   类似一种json的格式
    smtp.sendmail(sender,rec,message.as_string())
    smtp.close()
