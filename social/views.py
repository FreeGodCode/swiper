from django.shortcuts import render
from lib.http import render_json

from social.helper import recommend_users


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
    return render_json(None)


def dislike(request):
    """不喜欢"""
    return render_json(None)


def super_like(request):
    """超喜欢"""
    return render_json(None)


def regret(request):
    """反悔"""
    return render_json(None)


def show_liked_me(request):
    """显示喜欢我的"""
    return render_json(None)
