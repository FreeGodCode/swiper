from django.shortcuts import render
from lib.http import render_json


# Create your views here.
def index(request):
    return render_json(None)


def get_recommend_users(request):
    """获取推荐列表"""
    return render_json(None)


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
