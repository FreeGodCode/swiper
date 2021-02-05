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

    @classmethod
    def like(cls, uid, sid):
        obj = cls.objects.create(uid=uid, sid=sid, flag='like')
        return obj

    @classmethod
    def dislike(cls, uid, sid):
        obj = cls.objects.create(uid=uid, sid=sid, flag='dislike')
        return obj

    @classmethod
    def superlike(cls, uid, sid):
        obj = cls.objects.create(uid=uid, sid=sid, flag='superlike')
        return obj

    @classmethod
    def is_liked(cls, uid, sid):
        # 检查是否存在
        return cls.objects.filter(uid=uid, sid=sid, flag__in=['like', 'superlike']).exists()


class Friend(models.Model):
    """好友关系表"""
    # 好友关系是相互的
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friend(cls, uid1, uid2):
        uid1, uid2 = sorted([uid1, uid2])  # 排序
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)
