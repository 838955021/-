import requests,random

##请求地址
url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'

##APIID
account = 'C17579173'

#APIKEY
password = '1b51d4a8999500d431143563d1d39e81'

#收件人手机号
mobile = '13067062621'

##短信内容
num =random.randint(1000,9999)
content = '您的验证码是：1111。请不要把验证码泄露给其他人。'


#请求头
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}

##构建发送参数
data = {
    'account':account,
    'password':password,
    'mobile':mobile,
    'content':content,
}

##发送
response = requests.post(url,headers=headers,data=data)
#url 请求地址 #headers 请求头 #data 请求数据 内容

print(response.content.decode())