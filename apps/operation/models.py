from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.kol.models import Info as kol_info
from apps.note.models import Info as note_info

User = get_user_model()

class KolFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    kols = models.ForeignKey(kol_info, verbose_name="商品", help_text="商品id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户达人收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "kols")

    def __str__(self):
        return self.user.name

class NoteFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    notes = models.ForeignKey(note_info, verbose_name="笔记", help_text="笔记id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户笔记收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "notes")

    def __str__(self):
        return self.user.name