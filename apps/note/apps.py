from django.apps import AppConfig


class NoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.note'

    def ready(self):
        pass


# account/__init__.py中增加如下代码：
default_app_config = 'apps.note.apps.NoteConfig'