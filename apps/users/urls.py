from django.urls import path, include

# 导入 simplejwt 提供的几个验证视图类
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from apps.users.views import UserViewSet,EmailCodeViewSet

router = SimpleRouter()
router.register(r'user',UserViewSet,basename='user')
router.register(r'code',EmailCodeViewSet,basename='code')

# urls.py
urlpatterns = [
    # 登录
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
# 发送一封邮件
#     path('sendone/', send_one, name='one'),
] + router.urls

