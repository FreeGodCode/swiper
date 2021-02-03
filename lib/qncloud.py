# -*- coding: utf-8  -*-
# @Author: ty
# @File name: qncloud.py 
# @IDE: PyCharm
# @Create time: 2/3/21 12:15 PM
# @Description: 七牛云平台接入
from qiniu import Auth, put_file, etag

from swiper import config

# 构建鉴权对象, 设置为全局变量
# q = Auth(access_key, secret_key)
QN_AUTH = Auth(config.QN_ACCESS_KEY, config.QN_SECRET_KEY)


def upload_to_qiniu(localfile, key):
    """
    上传文件到七牛云
    params localfile: 要上传文件的本地路径
    params key: 上传到七牛后保存的文件名, 要上传的空间 bucket_name
    """
    # 生成上传token, 可以指定过期时间
    # token = q.upload_token(bucket_name, key, timeout)
    token = QN_AUTH.upload_token(config.QN_BUCKET, key, 3600)
    print(token)
    ret, info = put_file(token, key, localfile)
    # print(info)
    # ret 字典格式
    # ret = {'hash': '', 'key': ''}
    # info 是一个Response对象
    # 验证用
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
    return ret, info
