# -*- coding: utf-8  -*-
# @Author: ty
# @File name: helper.py 
# @IDE: PyCharm
# @Create time: 2/7/21 12:42 AM
# @Description: 权限装饰器
from common.code import NotHasPermission


def need_permission(permission_name):
    """
    权限检查装饰器
    :param permission_name:
    :return:
    """

    def check(view_func):
        # def wrapper(*args, **kwargs):
        def wrapper(request):
            user = request.user
            if user.vip.has_permission(permission_name):
                return view_func(request)
            else:
                raise NotHasPermission

        return wrapper

    return check
