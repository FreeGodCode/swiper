from django.shortcuts import render
from lib.http import render_json
from common import code
from lib.sms import check_verify_code

# Create your views here.
def get_verify_code(request):
    """
    获取验证码
    """
    # 获取手机号
    phone_num = request.GET.get('phone_num', '')

    # 产生验证码
    # 对接第三方短信平台发送短信验证码
    send_verify_code(phone_num)
    # return render_json(data, 200)
    # return render_json(None, code.OK)
    return render_json(None)


def login(request):
    """
    登录
    """
    # 获取参数
    phone_num = request.POST.get('phone_num', '')
    verify_code = request.POST.get('verify_code', '')
    # 验证参数
    if not check_verify_code(phone_num, verify_code):
        # 验证成功
        # pass
        # try:
        #     user = User.objects.get()
        # except User.DoesNotExist:
        #     User.objects.create()
        user, created = User.objects.get_or_create(phone_num=phone_num)
        # 缓存user id
        request.session['uid'] = user.id
        # return render_json(user.to_dict(), code.OK)
        return render_json(user.to_dict())
    else:
        # 验证失败, 返回错误的验证码
        return render_json(None, code.VCODE_ERROR)


def show_profile(request):
    """
    展示个人信息
    """
    return render_json()


def modify_profile(request):
    """
    编辑个人信息
    """
    return render_json()


def upload_avatar(request):
    """
    上传头像
    """
    return render_json()
