# -*- coding: utf-8  -*-
# @Author: ty
# @File name: urls.py 
# @IDE: PyCharm
# @Create time: 2/1/21 4:12 PM
# @Description:
urlpatterns = [
    url(r'^api/user/verify_code$', user.get_verify_code),
    url(r'^api/user/login$', user.login),
    url(r'^api/user/profile/show$', user.show_profile),
    url(r'^api/user/profile/modify$', user.modify_profile),
    url(r'^api/user/avatar/upload$', user.upload_avatar),
]