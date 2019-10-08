"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n&b=ckzx-&pgm1#y&%_&#nwf$j!9sw=g+f^m+4i5kn*kmdgb*c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Saller',
    'djcelery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

##收集静态文件
# STATIC_ROOT = os.path.join(BASE_DIR,'static')

#媒体文件的配置
MEDIA_URL = '/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,'static')

##公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyVsEgx2cOEBREZ28sqDz2M9sNxaOE8wllWSrA8zpyB0ItDcFfCRKwSEe/P90AGPgUQMVBOxmmVOxBawhNBO9Knx+O7mjXS4SZ/6LboNp611aV463axIMTfxU0CCXiOedIDh25ri7DKKue7gW43yE5T+ggf3w/VlYdxJPMTkYowsjbKsjw05YYoqP22BT+WKra5VkBpiM/SzUsCtzWpZoJGlHssC1hI5AKRQVe0VEerOYejK4SNLwGZeJrf8wUKFOQG7JBJnpx/J2m5PNqAk7OlJoHQf5BQsJfFLR+mWbuoBxNp4EmPTDJGKqONCSIGhPCEDhbSwc0nyAgntvnKQ76QIDAQAB
-----END PUBLIC KEY-----"""

##私钥
alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyVsEgx2cOEBREZ28sqDz2M9sNxaOE8wllWSrA8zpyB0ItDcFfCRKwSEe/P90AGPgUQMVBOxmmVOxBawhNBO9Knx+O7mjXS4SZ/6LboNp611aV463axIMTfxU0CCXiOedIDh25ri7DKKue7gW43yE5T+ggf3w/VlYdxJPMTkYowsjbKsjw05YYoqP22BT+WKra5VkBpiM/SzUsCtzWpZoJGlHssC1hI5AKRQVe0VEerOYejK4SNLwGZeJrf8wUKFOQG7JBJnpx/J2m5PNqAk7OlJoHQf5BQsJfFLR+mWbuoBxNp4EmPTDJGKqONCSIGhPCEDhbSwc0nyAgntvnKQ76QIDAQABAoIBAQCEujp/M0WGzt6hfhikpvQWNqReq797zVX45CLWnnx8LKdQI/S5oDKmm+6RVtJgb3Wt8Rop5Kq85y4JTy2T5m8LUoTjWbsV8QixBFlkv7tSKnciwDCno3346hv+FX3OAN7SHmZCMAMckR/y7aYozivL8eUbywjP99UYqDkLeVeEIOZeJj59XDbwdoyn9oirLLyORWhgwNOPHv57WSCzR6FFjSFh0/07oHgEkohioQB1NiiiaxVoBckZL+We9QbiH9bY6r+th95iCiK83SEAh7/xipD7Vg4Pc2xizqAdNISRh8XDF/ABfKchMN1WzpHNxjmDdBmptQp0GVdERZThf2wBAoGBAP05pmDiRTlZug56+L1YDT52fzk3HoiiQhY8jX8HYAeGZ4WDcG3RZZobyzh2pNdyTdT49cWkuiodSKTmV+gjVG6GO4S33R6Os+SuhmHOIAarZp7Da61Koe/IUaY/zhvrrIwPHWdBKVxNl//uXyzhhAn0IeMq5e2lmV/uT8zdWTQdAoGBAMuP3MTxkJYL9U+DRxAsNJLpsno6kBVTym0iUMxt5px2Sfdh0WxlPBBnfF2mtFGYMT/BmGXSlaNKGQvBbWkJCouTIImPcUAql6rqZf2wtZ+MlUzrA8ck+T5cC8XT4UExvcKTy2e3e4Q+kQbI2vfZ3cd8hrzZgu+YYn2zel9jA0U9AoGAMTbAGDpBm+jNWT0bFKmFQWuERFlrDMEEORAhq9uCFVRQ0EkAU8eLiIz4TQv584laiRatpXDjYYX5dVrzIMGlCin6bUvSpLq1Sa+FnIKUBNfRBPAUAETt/g0fmUDzTMfb7AiP/V5TrIXEEdCBHNbjc4/H+j9/GlXB3jwRtE4cpR0CgYEApo2g/ur/eCV0o4gv/sWMhp/7zhJYjXqvZ7fqEDnjtCT8xBIe/eeey3VAxod9hj1WHmpSPQ2eLaqU749l68jf/e91cdgRu4Sd79Q1euq40ECAcBziTHCuFh3N7CE+bs86ChhPFx+DSmK+2qRAtQZnda8ntyDpBwzRmTPebmle5akCgYB+Q0CwnPIrhqTmvOv2AMnqhZ5zcW5JqswFikOqgW74n0sJPV/g9xHUBk31WV/feFjn5tRrsZ1++WgmYDKsE5wwQi/VnaHVmJG2RHLuIjR1915t3f2R4xl0shKzRiVjbwHhWghGTRi0TE/THtgC9E2Z4gw0Aclmj0jP1Iia6DwIAA==
-----END RSA PRIVATE KEY-----"""


import djcelery     ###导入djcelery包
djcelery.setup_loader()    ##进行模块载入
BROKER_URL = 'redis://127.0.0.1:6379/1'   ##中间件 中间人  指定redis
CELERY_IMPORTS = ('CeleryTask.tasks')  ##具体的任务文件
CELERY_TIMEZONE = 'Asia/Shanghai'   ##celery时区   跟django保持一致
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'   ##django-celery处理器  是固定的


from celery.schedules import timedelta

CELERYBEAT_SCHEDULE = {
    u'测试任务': {
        'task':'CeleryTask.tasks.test',   ## 任务函数
        'schedule':timedelta(seconds=1)    ##执行时间

    }
}

