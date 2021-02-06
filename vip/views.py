from django.shortcuts import render

from lib.http import render_json

from vip.models import Vip


# Create your views here.
def index(request):
    return render_json(None)


def show_vip_permissions(request):
    """
    展示VIP所拥有的权限
    :param request:
    :return:
    """
    vip_permissions = []
    # vips = Vip.objects.filter(level__gte=1)  # 普通用户的等级为1
    for vip in Vip.objects.filter(level__gte=1):
        vip_info = vip.to_dict()
        permission_info = []
        for permission in vip.permissions:
            permission_info.append(permission.to_dict())
        vip_info['permission_info'] = permission_info
    return render_json(vip_info)
