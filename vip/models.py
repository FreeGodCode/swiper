from django.db import models


# Create your models here.
class Vip(models.Model):
    """VIP表"""
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField(unique=True)
    price = models.FloatField()


class Permission(models.Model):
    """权限表"""
    name = models.CharField(max_length=32)
    desc = models.TextField()


class VipPermissionRelation(models.Model):
    """vip和权限关联表"""
    vip_id = models.IntegerField()
    permission_id = models.IntegerField()
