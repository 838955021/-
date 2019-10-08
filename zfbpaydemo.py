from alipay import AliPay


##公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyVsEgx2cOEBREZ28sqDz2M9sNxaOE8wllWSrA8zpyB0ItDcFfCRKwSEe/P90AGPgUQMVBOxmmVOxBawhNBO9Knx+O7mjXS4SZ/6LboNp611aV463axIMTfxU0CCXiOedIDh25ri7DKKue7gW43yE5T+ggf3w/VlYdxJPMTkYowsjbKsjw05YYoqP22BT+WKra5VkBpiM/SzUsCtzWpZoJGlHssC1hI5AKRQVe0VEerOYejK4SNLwGZeJrf8wUKFOQG7JBJnpx/J2m5PNqAk7OlJoHQf5BQsJfFLR+mWbuoBxNp4EmPTDJGKqONCSIGhPCEDhbSwc0nyAgntvnKQ76QIDAQAB
-----END PUBLIC KEY-----"""


##私钥
alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyVsEgx2cOEBREZ28sqDz2M9sNxaOE8wllWSrA8zpyB0ItDcFfCRKwSEe/P90AGPgUQMVBOxmmVOxBawhNBO9Knx+O7mjXS4SZ/6LboNp611aV463axIMTfxU0CCXiOedIDh25ri7DKKue7gW43yE5T+ggf3w/VlYdxJPMTkYowsjbKsjw05YYoqP22BT+WKra5VkBpiM/SzUsCtzWpZoJGlHssC1hI5AKRQVe0VEerOYejK4SNLwGZeJrf8wUKFOQG7JBJnpx/J2m5PNqAk7OlJoHQf5BQsJfFLR+mWbuoBxNp4EmPTDJGKqONCSIGhPCEDhbSwc0nyAgntvnKQ76QIDAQABAoIBAQCEujp/M0WGzt6hfhikpvQWNqReq797zVX45CLWnnx8LKdQI/S5oDKmm+6RVtJgb3Wt8Rop5Kq85y4JTy2T5m8LUoTjWbsV8QixBFlkv7tSKnciwDCno3346hv+FX3OAN7SHmZCMAMckR/y7aYozivL8eUbywjP99UYqDkLeVeEIOZeJj59XDbwdoyn9oirLLyORWhgwNOPHv57WSCzR6FFjSFh0/07oHgEkohioQB1NiiiaxVoBckZL+We9QbiH9bY6r+th95iCiK83SEAh7/xipD7Vg4Pc2xizqAdNISRh8XDF/ABfKchMN1WzpHNxjmDdBmptQp0GVdERZThf2wBAoGBAP05pmDiRTlZug56+L1YDT52fzk3HoiiQhY8jX8HYAeGZ4WDcG3RZZobyzh2pNdyTdT49cWkuiodSKTmV+gjVG6GO4S33R6Os+SuhmHOIAarZp7Da61Koe/IUaY/zhvrrIwPHWdBKVxNl//uXyzhhAn0IeMq5e2lmV/uT8zdWTQdAoGBAMuP3MTxkJYL9U+DRxAsNJLpsno6kBVTym0iUMxt5px2Sfdh0WxlPBBnfF2mtFGYMT/BmGXSlaNKGQvBbWkJCouTIImPcUAql6rqZf2wtZ+MlUzrA8ck+T5cC8XT4UExvcKTy2e3e4Q+kQbI2vfZ3cd8hrzZgu+YYn2zel9jA0U9AoGAMTbAGDpBm+jNWT0bFKmFQWuERFlrDMEEORAhq9uCFVRQ0EkAU8eLiIz4TQv584laiRatpXDjYYX5dVrzIMGlCin6bUvSpLq1Sa+FnIKUBNfRBPAUAETt/g0fmUDzTMfb7AiP/V5TrIXEEdCBHNbjc4/H+j9/GlXB3jwRtE4cpR0CgYEApo2g/ur/eCV0o4gv/sWMhp/7zhJYjXqvZ7fqEDnjtCT8xBIe/eeey3VAxod9hj1WHmpSPQ2eLaqU749l68jf/e91cdgRu4Sd79Q1euq40ECAcBziTHCuFh3N7CE+bs86ChhPFx+DSmK+2qRAtQZnda8ntyDpBwzRmTPebmle5akCgYB+Q0CwnPIrhqTmvOv2AMnqhZ5zcW5JqswFikOqgW74n0sJPV/g9xHUBk31WV/feFjn5tRrsZ1++WgmYDKsE5wwQi/VnaHVmJG2RHLuIjR1915t3f2R4xl0shKzRiVjbwHhWghGTRi0TE/THtgC9E2Z4gw0Aclmj0jP1Iia6DwIAA==
-----END RSA PRIVATE KEY-----"""


###实例化支付对象
alipay = AliPay(
        appid=2016101300673952,
        app_notify_url= None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
)

##实例化订单
order_string = alipay.api_alipay_trade_page_pay(
    subject='速效生发液', ##交易主题
    out_trade_no=10000000001,   ##订单号
    total_amount='1000',    ###交易总金额
    return_url=None,       ##请求支付，之后及时回调的一个借口
    notify_url=None,       ###通知地址，
)


##    发送支付请求
##   请求地址  支付网关 + 实例化订单
result = 'https://openapi.alipaydev.com/gateway.do?'+order_string
print(result)
