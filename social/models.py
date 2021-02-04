from django.db import models


# Create your models here.
class Swiped(models.Model):
    """滑动记录表"""
    FLAGS = (
        ('superlike', '上滑'),
        ('like', '右滑'),
        ('dislike', '左滑'),
    )
    uid = models.IntegerField(verbose_name='滑动者的ID')
    sid = models.IntegerField(verbose_name='被滑动者的ID')
    flag = models.CharField(max_length=10, choices=FLAGS)  # 滑动标志
    date_time = models.DateTimeField(auto_now=True)  # 滑动的时间


class Friend(models.Model):
    """好友关系表"""
    # 好友关系是相互的
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()
