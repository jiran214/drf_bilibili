from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    print('保存成功')
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()

# 清除老缓存
# @receiver(post_delete, sender=MyModel)
# def cache_post_delete_handler(sender, **kwargs):
#      cache.delete('cached_objects')
#
# @receiver(post_save, sender=MyModel)
# def cache_post_save_handler(sender, **kwargs):
#     cache.delete('cached_objects')
