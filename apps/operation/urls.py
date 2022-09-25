from rest_framework.routers import SimpleRouter

from apps.operation.views import NoteFavViewSet,KolFavViewSet

router = SimpleRouter()
router.register(r'notefav',NoteFavViewSet,basename='notefav')
router.register(r'kolfav',KolFavViewSet,basename='kolfav')

urlpatterns = [
]

urlpatterns+=router.urls


