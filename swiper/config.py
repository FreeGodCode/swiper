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

