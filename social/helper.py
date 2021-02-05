# -*- coding: utf-8  -*-
# @Author: ty
# @File name: helper.py 
# @IDE: PyCharm
# @Create time: 2/4/21 6:33 PM
# @Description: 逻辑处理函数
import datetime

from social.models import Swiped, Friend
from user.models import User


def recommend_users(user):
    """
    推荐的人
    :return:
    """
    dating_sex = user.profile.dating_sex
    location = user.profile.location
    min_dating_age = user.profile.min_dating_age
    max_dating_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    min_year = current_year - max_dating_age
    max_year = current_year - min_dating_age
    users = User.objects.filter(sex=dating_sex, location=location, birth_year__gte=min_year, birth_year__lte=max_year)
    return users


def like_someone(user, sid):
    """

    :param user:
    :param sid:
    :return:
    """
    Swiped.like(user.id, sid)
    # 检查对方是否喜欢自己
    if Swiped.is_liked(sid, user.id):
        Friend.make_friend(uid1=user.id, uid2=sid)
        return True
    else:
        return False
