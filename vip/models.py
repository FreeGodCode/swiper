from django.db import models

from lib.orm import ModelMixin


# Create your models here.
class Vip(models.Model, ModelMixin):
    """VIP表"""
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField(unique=True)
    price = models.FloatField()

    @property
    def permissions(self):
        """查询关联的权限信息"""
        relations = VipPermissionRelation.objects.filter(vip_id=self.id)
        permission_id_list = [r.permission_id for r in relations]
        return Permission.objects.filter(id__in=permission_id_list)

    class Meta:
        db_table = 'db_vip'
        ordering = ['level']
        verbose_name = 'vip'
        verbose_name_plural = verbose_name


class Permission(models.Model, ModelMixin):
    """权限表"""
    name = models.CharField(max_length=32)
    desc = models.TextField()

    class Meta:
        db_table = 'db_permission'
        ordering = ['name']
        verbose_name = 'permission'
        verbose_name_plural = verbose_name


class VipPermissionRelation(models.Model, ModelMixin):
    """vip和权限关联表"""
    vip_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = 'db_vip_permission'
