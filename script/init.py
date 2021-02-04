import os
import sys
import random

import django

# 设置环境
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')
django.setup()

from user.models import User

from vip.models Vip, Permission, VipPermRelation

last_names = ()

first_names = {
    '男': [],
    '女': [],
}


def random_name():
    """随机生成人名"""
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name, first_name]), sex


def create_robots(n):
    """创建初始用户"""
    for i in range(n):
        name, sex = random_name()
        try:
            User.objects.create(
                phone_num='%s' % random.randrange(21000000000, 21900000000),
                nickname=name,
                sex=sex,
                birth_year=random.randint(1980, 2000),
                birth_month=random.randint(1, 12),
                birth_day=random.randint(1, 28),
                location=random.choice(['BJ', 'SH', 'SZ', 'WH', 'CD', 'XA'])
            )
            print('created: %s %s' % (name, sex))
        except django.db.utils.IntegerityError:
            pass


def init_permission():
    """
    创建权限模型
    :return:
    """
    permission_names = [
        'vipflag',
        'superlike',
        'regret',
        'anylocation',
        'unlimit_like',
    ]
    for name in permission_names:
        permission, _ = Permission.objects.get_or_create(name=name)
        print('create permission {}'.format(permission.name))

def init_vip():
    """

    :return:
    """
    for i in range(4):
        vip, _ = Vip.objects.get_or_create(name='会员{}'.format(i), level=i, price=i*5)
        print('create {}'.format(vip.name))


def create_vip_permission_relations():
    """
    创建vip和permission的关系
    :return:
    """
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    vipflag = Permission.objects.get(name='vipflag')
    superlike = Permission.objects.get(name='superlike')
    regret = Permission.objects.get(name='regret')
    anylocation = Permission.objects.get(name='anylocation')
    unlimit_like = Permission.objects.get(name='unlimit_like')
    # vip1权限
    VipPermRelation.objects.get_or_create(vip_id = vip1.id, perm_id = vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id = vip1.id, perm_id = superlike.id)
    # vip2权限
    VipPermRelation.objects.get_or_create(vip_id = vip2.id, perm_id = vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id = vip2.id, perm_id = regret.id)
    # vip3权限
    VipPermRelation.objects.get_or_create(vip_id = vip3.id, perm_id = vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id = vip3.id, perm_id = superlike.id)
    VipPermRelation.objects.get_or_create(vip_id = vip3.id, perm_id = regret.id)
    VipPermRelation.objects.get_or_create(vip_id = vip3.id, perm_id = anylocation.id)
    VipPermRelation.objects.get_or_create(vip_id = vip3.id, perm_id = unlimit_like.id)


if __name__ == '__main__':
    create_robots(1000)
    # init_permission()
    # init_vip()
    # create_vip_permission_relations()
