
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from bilibili import settings
from apps.kol import urls as kol_urls
from apps.note import urls as note_urls
from apps.users import urls as user_urls
from apps.operation import urls as oper_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(kol_urls)),
    path('', include(note_urls)),
    path('', include(user_urls)),
    path('', include(oper_urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
