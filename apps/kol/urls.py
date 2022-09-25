from rest_framework.routers import SimpleRouter

from apps.kol.views import KolInfoViewSet

router = SimpleRouter()
router.register(r'kol',KolInfoViewSet)
urlpatterns = [
]
urlpatterns+=router.urls
