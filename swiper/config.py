# -*- coding: utf-8  -*-
# @Author: ty
# @File name: config.py 
# @IDE: PyCharm
# @Create time: 2/1/21 5:02 PM
# @Description: 其他配置

# 互亿无线短信平台对接配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': '',
    'password': '',
    'content': '您的验证 码是: %s, 为了您的帐号安全, 请勿泄露您的验证码.',
    'mobile': None,
    'format': 'json',
}

# 七牛云配置
QN_BUCKET = 'swiper_space'
QN_BASE_URL = 'http://qnwvltezo.hn-bkt.clouddn.com'
QN_ACCESS_KEY = 'rAl8TwaBg3dzgBZx2qyEV9ap9UbVy7k5vioqRBKR'
QN_SECRET_KEY = 'Yy0AfVCsdM4hvvu3Wa1mpWtDv7-IEvEcY0BE8uyJ'
