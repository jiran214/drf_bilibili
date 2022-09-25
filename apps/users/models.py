from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='性名')  # blank为true是 提交表单可以为空
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', '女')), default='female',
                              verbose_name='性别')  # choices 单选属性
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name='电话')
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name='邮箱')
    image = models.ImageField(upload_to='avatar/%Y/%m', null=True, blank=True, verbose_name='头像')

    vip_choices = ((0, '普通用户'), (1, 'vip'), (2, 'svip'), (3, 'sss'))
    vip = models.IntegerField(choices=vip_choices,default = 0)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'  # 模型类的复数名

    def __str__(self):
        # 调用对象返回字符串
        return self.username