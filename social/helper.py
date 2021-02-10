# -*- coding: utf-8  -*-
# @Author: ty
# @File name: helper.py 
# @IDE: PyCharm
# @Create time: 2/4/21 6:33 PM
# @Description: 逻辑处理函数
import datetime

from lib.cache import rds
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


def super_like_someone(user, sid):
    """

    :param user:
    :param sid:
    :return:
    """
    Swiped.superlike(user.id, sid)
    # 检查对方是否喜欢自己
    if Swiped.is_liked(sid, user.id):
        Friend.make_friend(uid1=user.id, uid2=sid)
        return True
    else:
        return False


def regreted(user):
    # 反悔
    # 取出最后一次滑动记录
    swiped = Swiped.objects.filter(uid=user.id).latest()
    # 删除好友记录
    if swiped.flag in ['like', 'superlike']:
        Friend.break_off(user.id, swiped.sid)
    # 删除滑动记录
    swiped.delete()


def users_liked_me(user):
    """"""
    swipes = Swiped.liked_me(user.id)
    swiper_uid_list = [s.uid for s in swipes]
    return User.objects.filter(id__in=swiper_uid_list)


def add_swipe_score(uid, flag):
    """
    增加滑动排行
    :param uid:
    :param flag:
    :return:
    """
    score = {'like': 5, 'superlike': 7, 'dislike': -5}[flag]
    rds.zincrby('HotSwiped', uid, score)
