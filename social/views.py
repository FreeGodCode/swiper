from django.shortcuts import render
from lib.http import render_json

from social.helper import recommend_users, like_someone, super_like_someone, regreted, users_liked_me, add_swipe_score

from social.models import Swiped
from vip.helper import need_permission


# Create your views here.
def index(request):
    return render_json(None)


def get_recommend_users(request):
    """获取推荐列表"""
    # 分页处理
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page

    user = request.user
    users = recommend_users(user)[start: end]  # 懒加载
    result = [user.to_dict() for user in users]
    return render_json(result)


def like(request):
    """喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    is_matched = like_someone(user, sid)
    add_swipe_score(sid, 'like')  # 添加滑动排行
    return render_json({'is_matched': is_matched})


def dislike(request):
    """不喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    Swiped.dislike(user.id, sid)
    add_swipe_score(sid, 'dislike')  # 添加滑动排行
    return render_json(None)


@need_permission('super_like')
def super_like(request):
    """超喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    is_matched = super_like_someone(user, sid)
    add_swipe_score(sid, 'superlike')  # 添加滑动排行
    return render_json({'is_matched': is_matched})


@need_permission('regret')
def regret(request):
    """反悔"""
    regreted(request.user)
    return render_json(None)


@need_permission('show_liked_me')
def show_liked_me(request):
    """显示喜欢我的"""
    users = users_liked_me(request.user)
    result = [u.to_dict() for u in users]
    return render_json({'result': result})


def get_friends(request):
    """获取好友列表"""
    result = [friend.to_dict() for friend in request.user.friends()]
    return render_json(result)
