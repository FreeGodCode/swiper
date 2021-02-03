# -*- coding: utf-8  -*-
# @Author: ty
# @File name: helper.py 
# @IDE: PyCharm
# @Create time: 2/1/21 4:54 PM
# @Description: 逻辑处理函数
import os

from django.conf import settings


def save_upload_file(user, upload_file):
    """
    将上传的文件保存到本地
    """
    # 文件名不需要文件后缀去识别文件的类型
    filename = 'avatar_%s' % user.id
    # 拼接文件路径
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    # 文件写入
    with open(filepath, 'wb') as f:
        for chunk in upload_file.chunks():  # chunks 实现时生成器的方式实现的 yield
            f.write(chunk)

    return filepath, filename
