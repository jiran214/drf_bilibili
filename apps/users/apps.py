from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

# account/__init__.py中增加如下代码：
default_app_config = 'apps.users.apps.UserConfig'