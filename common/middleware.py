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

    def process_request(self, request):
        """

        """
        # 获取用户信息
        uid = request.session.get['uid']
        # 验证用户信息
        if uid is None:
            return render_json(None, code.LOGIN_REQUIRE)
        user = User.objects.get(uid)
