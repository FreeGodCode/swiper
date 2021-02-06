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

from vip.models import Vip, Permission, VipPermissionRelation

# 姓式
last_names = (
    '赵', '钱', '孙', '李', '周', '吴', '郑', '王',
    '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨',
    '朱', '秦', '尤', '许', '何', '吕', '施', '张',
    '孔', '曹', '严', '华', '金', '魏', '陶', '姜',
    '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
    '云', '苏', '潘', '葛', '奚', '范', '彭', '郎',
    '鲁', '韦', '昌', '马', '苗', '凤', '花', '方',
    '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐',
    '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤',
    '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
    '乐', '于', '时', '傅', '皮', '卞', '齐', '康',
    '伍', '余', '元', '卜', '顾', '孟', '平', '黄',
    '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪',
    '祁', '毛', '禹', '狄', '米', '贝', '明', '臧',
    '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
    '熊', '纪', '舒', '屈', '项', '祝', '董', '梁',
    '杜', '阮', '蓝', '闵', '席', '季', '麻', '强',
    '贾', '路', '娄', '危', '江', '童', '颜', '郭',
    '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆',
    '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍',
    '虞', '万', '支', '柯', '昝', '管', '卢', '莫',
    '经', '房', '裘', '缪', '干', '解', '应', '宗',
    '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪',
    '包', '诸', '左', '石', '崔', '吉', '钮', '龚',
    '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁',
    '荀', '羊', '於', '惠', '甄', '曲', '家', '封',
    '芮', '羿', '储', '靳', '汲', '邴', '糜', '松',
    '井', '段', '富', '巫', '乌', '焦', '巴', '弓',
    '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬',
    '全', '郗', '班', '仰', '秋', '仲', '伊', '宫',
    '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎',
    '祖', '武', '符', '刘', '景', '詹', '束', '龙',
    '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄',
    '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂',
    '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙',
    '池', '乔', '阴', '鬱', '胥', '能', '苍', '双',
    '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄',
    '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍',
    '卻', '璩', '桑', '桂', '濮', '牛', '寿', '通',
    '边', '扈', '燕', '冀', '郏', '浦', '尚', '农',
    '温', '别', '庄', '晏', '柴', '瞿', '阎', '充',
    '慕', '连', '茹', '习', '宦', '艾', '鱼', '容',
    '向', '古', '易', '慎', '戈', '廖', '庾', '终',
    '暨', '居', '衡', '步', '都', '耿', '满', '弘',
    '匡', '国', '文', '寇', '广', '禄', '阙', '东',
    '欧', '殳', '沃', '利', '蔚', '越', '夔', '隆',
    '师', '巩', '厍', '聂', '晁', '勾', '敖', '融',
    '冷', '訾', '辛', '阚', '那', '简', '饶', '空',
    '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰',
    '巢', '关', '蒯', '相', '查', '后', '荆', '红',
    '游', '竺', '权', '逯', '盖', '益', '桓', '公',
    '万', '俟', '司', '马', '上', '官', '欧', '阳',
    '夏', '侯', '诸', '葛', '闻', '人', '东', '方',
    '赫', '连', '皇', '甫', '尉', '迟', '公', '羊',
    '澹', '台', '公', '冶', '宗', '政', '濮', '阳',
    '淳', '于', '单', '于', '太', '叔', '申', '屠',
    '公', '孙', '仲', '孙', '轩', '辕', '令', '狐',
    '钟', '离', '宇', '文', '长', '孙', '慕', '容',
    '鲜', '于', '闾', '丘', '司', '徒', '司', '空',
    '丌', '官', '司', '寇', '仉', '督', '子', '车',
    '颛', '孙', '端', '木', '巫', '马', '公', '西',
    '漆', '雕', '乐', '正', '壤', '驷', '公', '良',
    '拓', '跋', '夹', '谷', '宰', '父', '谷', '梁',
    '晋', '楚', '闫', '法', '汝', '鄢', '涂', '钦',
    '段', '干', '百', '里', '东', '郭', '南', '门',
    '呼', '延', '归', '海', '羊', '舌', '微', '生',
    '岳', '帅', '缑', '亢', '况', '郈', '有', '琴',
    '梁', '丘', '左', '丘', '东', '门', '西', '门',
    '商', '牟', '佘', '佴', '伯', '赏', '南', '宫',
    '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟',
)

# 名字
first_names = {
    '男': [
        '泉修', '绩翰', '清载', '众天', '洪释', '幽统', '吉福', '章帆', '坤旷', '耿顷', '韬镜', '信尧', '闲轩', '理莫', '苑谦', '嘉苑', '材翰',
        '易坚', '千毅', '云耀', '腾蓝', '知建', '羽西', '馨龙', '智沧', '谷信', '奥材', '岸疏', '浦余', '深烟', '柯兼', '捷硕', '波楷', '霖尘',
        '蒙铭', '昂源', '韶若', '理弥', '芹贤', '勤福', '源循', '圣盛', '境晖', '若岩', '励杭', '峰乾', '瀚尘', '棕乾', '浪常', '齐益', '游云',
        '奥易', '存翱', '天均', '芹量', '济彬', '群韵', '桐循', '浪瑜', '华旭', '昙劲', '若耀', '泉霖', '进尧', '奥际', '融铭', '劲勇', '何晟',
        '刚浪', '初庆', '遥毅', '境铭', '昂阔', '敬宜', '神忆', '彬深', '旷何', '昌恩', '贤钦', '浅依', '林翼', '顷勤', '烨泽', '幽秉', '柯茂',
        '林恒', '传宸', '超贵', '晨泽', '龙镇', '峰封', '玮风', '天柏', '慈展', '庸民', '浅阔', '宇合', '明兼', '杉帅', '全征', '耕瀚', '朋意',
        '玄劲', '启彦', '勇祖', '修煜', '顷厚', '秋宏', '均祖', '境哲', '奉利', '怀瑾', '鸽循', '坤舟', '宇如', '誓常', '勤欢', '晨迪', '毅引',
        '合少', '腾松', '统慈', '飞彰', '展载', '朋文', '嘉肖', '福群', '生秉', '杭本', '腾里', '昆乾', '奔润', '鹤树', '勉捷', '恭凌', '琪彤',
        '宏布', '齐锦', '刚远', '云锋', '朴钟', '钦意', '林散', '裕绍', '肃瀚', '照晋', '方刊', '紫迁', '千君', '奔悟', '睿畅', '满路', '钱腾',
        '帅煜', '散玮', '昙义', '聪沧', '凌柏', '玉励', '熙柯', '韵伟', '久林', '晴镜', '风玮', '深奉', '岳腾', '高杉', '康净', '远资', '建烟',
        '明秀', '宝琪', '元任', '桐蒙', '桦鼎', '城硕', '帅肃', '棋妙', '慈妙', '锐弥', '煊朴', '昆幽', '语霄', '振万', '景盛', '观昂', '玉勤',
        '路琦', '淡久', '缈柯', '道言', '齐昙', '意歌', '观谷', '深震', '统浩', '绍彰', '鸽玉', '望桐', '拂贵', '镇松', '福秉', '兼坚', '致实',
        '山方', '壤利', '影星', '湛达', '雷劲', '晴义', '鸽钟', '悠益', '淡瑾', '烟瑜', '合进', '千歌', '飘易', '论翱', '治德', '笃浪', '翎唯',
        '阜山', '润勤', '振云', '境固', '奉如', '豪易', '博紫', '向月', '聚桦', '民秀', '钟睿', '兼施', '桐耕', '知奇', '铁初', '壮全', '里吟',
        '琢田', '悠永', '邦折', '铭峰', '晴耿', '引引', '益誓', '如扬', '风来', '硕乐', '绘云', '幽鸣', '鉴城', '渊本', '勋裕', '原乾', '祥石',
        '极乔', '翰含', '凯擎', '永豫', '耀励', '刚玄', '宁临', '浪蓝', '腾悠', '耀冬', '泉义', '忠恒', '龙章', '博含', '疏玮', '基资', '卡翼',
        '潭城', '舟任', '望寒', '净莫', '煊慎', '帆洪', '鼎沧', '博建', '凯迪', '统益', '昂挚', '唯佑', '奇皓', '东勤', '晓瑞', '里昂', '庸琢',
        '启复', '生延', '挚折', '苑朴', '畅古', '洋然', '初鼎', '育韶', '鹏庭', '玉境', '晋磊', '睿寒',
    ],
    '女': [
        '瑞绣', '诗柯', '晓兰', '丽姝', '曼丽', '雅琪', '丽华', '晴柔', '晓玉', '欢梦', '芷纹', '睿婕', '晶玉', '哓怡', '雅琴', '虹娜', '菲颖',
        '婧琪', '梓欣', '诗茵', '曼倚', '静秋', '寒荷', '清怡', '乐悦', '寒珊', '晗玥', '碧玉', '君韵', '信怡', '晓燕', '巧凤', '婉如', '焓瑛',
        '子凤', '楚怡', '自红', '慧英', '秀丽', '如洁', '含雪', '嘉洁', '柏倚', '朝霞', '艳文', '灵慧', '秀荧', '嘉芬', '若绮', '英珊', '沁洁',
        '英桐', '海倩', '邑芙', '紫淑', '梅月', '兰茹', '彩媛', '梨珺', '靖雯', '曼芸', '婕茜', '熙惠', '紫惠', '紫芸', '曼芙', '娅艳', '若媛',
        '珠媛', '梨芙', '莺芳', '敏芸', '雪芙', '诗淑', '暄晗', '紫华', '曼倚', '英芙', '飞妍', '婕曦', '彩睿', '莉雁', '彩鸣', '微雅', '珠宸',
        '旋菲', '海露', '曼涵', '蓉清', '琪雅', '若芷', '娉诺', '婉瑜', '凝昱', '曼舒', '若玲', '彩雅', '紫媛', '莺月', '婉舒', '若菡', '思玥',
        '婕菲', '梨晴', '曼絮', '娅茹', '曼珊', '婕清', '若茜', '彩馨', '雨雁', '婵楦', '英娜', '紫宸', '苑诗', '虞清', '梅清', '婧倩', '曼恬',
        '琳雯', '思梓', '梨菡', '樱桃', '悦馨', '熙茜', '枫语', '榆雅', '艺鸣', '姝瑶', '紫睿', '卿芸', '雪纹', '迎茹', '琴雯', '彩宸', '燕婷',
        '熙婷', '敏惠', '艺芙', '佳歆', '榆惠', '婉鸣', '筠惠', '莉翔', '筠茜', '梅辰', '婌琳', '梅雯', '彩芝', '紫婷', '婕岚', '熙云', '琪雁',
        '熙珺', '海桃', '梅舒', '卿瑛', '旋惠', '梨翔', '梨瑜', '诗雯', '海宸', '昱娴', '霞蕴', '梅菲', '莉雅', '寄梦', '虞絮', '涵悦', '雪桑',
        '艺嫣', '甜夏', '英岚', '紫芙', '瑶茜', '梅雅', '映倩', '紫云', '问珊', '若雅', '琦惠', '烟絮', '海菡', '舒鹭', '婉云', '琳珺', '紫翠',
        '婉惠', '若蓝', '婕雅', '婕珊', '琦雅', '曼雯', '雪嘉', '婉寒', '海嫣', '怡雪', '紫舒', '曼芷', '婕碧', '卿珊', '梨菱', '雪玲', '珠瑜',
        '婉凌', '琦淑', '映文', '艺菲', '英曦', '紫瑛', '敏茹', '雪雅', '珠清', '微茜', '海瑛', '珠芙', '沛芳', '紫芬', '若晴', '素颖', '雪晴',
        '诗惠', '诗雅', '问雁', '迎菡', '海蓝', '婕娜', '艺纹', '紫蓝', '熙淑', '荷晴', '觅茜', '若茹', '含芸', '筠岚', '紫雅', '忻红', '艺芝',
        '娅珍', '笛琴', '诗婷', '卿娜', '英月', '婉茹', '卿惠', '雪睿', '雪絮',
    ],
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
        ('vipflag', '会员身份标识'),
        ('superlike', '超级喜欢'),
        ('regret', '反悔'),
        ('anylocation', '任意更改定位'),
        ('(unlimit_like', '无限喜欢次数'),
        ('show_liked_me', '查看喜欢过我的人'),
    ]
    for name, desc in permission_names:
        permission, _ = Permission.objects.get_or_create(name=name, desc=desc)
        print('create permission {}'.format(permission.name))


def init_vip():
    """

    :return:
    """
    for i in range(4):
        vip, _ = Vip.objects.get_or_create(name='{}级会员'.format(i), level=i, price=i * 5)
        print('create {}'.format(vip.name))


def create_vip_permission_relations():
    """
    创建vip和permission的关系
    :return:
    """
    # 获取VIP
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    vipflag = Permission.objects.get(name='vipflag')
    superlike = Permission.objects.get(name='superlike')
    regret = Permission.objects.get(name='regret')
    anylocation = Permission.objects.get(name='anylocation')
    unlimit_like = Permission.objects.get(name='unlimit_like')
    show_liked_me = Permission.objects.get(name='show_liked_me')
    # vip1权限
    VipPermissionRelation.objects.get_or_create(vip_id=vip1.id, perm_id=vipflag.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip1.id, perm_id=superlike.id)
    # vip2权限
    VipPermissionRelation.objects.get_or_create(vip_id=vip2.id, perm_id=vipflag.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip2.id, perm_id=superlike.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip2.id, perm_id=regret.id)
    # vip3权限
    VipPermissionRelation.objects.get_or_create(vip_id=vip3.id, perm_id=vipflag.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip3.id, perm_id=superlike.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip3.id, perm_id=regret.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip3.id, perm_id=anylocation.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip3.id, perm_id=unlimit_like.id)
    VipPermissionRelation.objects.get_or_create(vip_id=vip3.id, perm_id=show_liked_me.id)


if __name__ == '__main__':
    create_robots(1000)
    # init_permission()
    # init_vip()
    # create_vip_permission_relations()
