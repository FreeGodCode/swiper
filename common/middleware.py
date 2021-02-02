# -*- coding: utf-8  -*-
# @Author: ty
# @File name: middleware.py 
# @IDE: PyCharm
# @Create time: 2/2/21 11:19 AM
# @Description: 自定义中间件

from django.utils.deprecation import MiddlewareMixin
from common import code
from user.models import User
from lib.http import render_json


class AuthMiddleware(MiddlewareMixin):
    """用户验证中间件"""
    # 白名单
    white_list = [
        '/api/user/verify_code',
        '/api/user/login',
    ]

    def process_request(self, request):
        """
        所有请求处理之前都要进行中间件的处理
        """
        # 检查当前path是否在白名单内
        if request.path in self.white_list:
            return

        # 用户登录验证
        # 获取用户信息
        uid = request.session.get['uid']
        # 验证用户信息
        if uid is None:
            return render_json(None, code.LOGIN_REQUIRE)
        else:
            try:
                user = User.objects.get(uid)
            # 用户不存在
            except User.DoesNotExist:
                return render_json(None, code.USER_NOT_EXIST)
            else:
                # 最终将user对象附到request上
                request.user = user
