from django.db import models


# Create your models here.
class User(models.Model):
    """用户模型类"""
    SEX = (
        ('0', '男性'),
        ('1', '女性'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phone_num = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)
    # 出生年月日
    birth_year = models.IntegerField(default=1998, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')

    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=32, verbose_name='常居地')


class Profile(models.Model):
    """个人配置数据"""
    SEX = (
        ('0', '男'),
        ('1', '女'),
    )
    location = models.CharField(max_length=32, verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=60, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配性别')
    vibration = models.CharField(max_length=8, default=True, verbose_name='开启提示')
    only_matche = models.CharField(max_length=8, default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.CharField(max_length=8, default=True, verbose_name='自动播放视频')
