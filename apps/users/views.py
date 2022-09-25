from random import Random

from django.contrib.auth import get_user_model

# Create your views here.
from django.http import HttpResponse
from django_redis import get_redis_connection
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.ser import UserDetailSer, EmailSer, UserRegSer

from apps.users import tasks

User = get_user_model()


class UserViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSer
        elif self.action == 'create':
            return UserRegSer
        else:
            return UserDetailSer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        re_dict["token"] = access_token
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


def random_str(randomlength=4):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str  # 将拼接的字符串返回


class EmailCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EmailSer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = random_str(4)
        redis = get_redis_connection()
        redis.set(email, code, 120)

        tasks.send_mail_task.delay("593848579@qq.com", "chen", code)
        return Response({"email": email, "code": code}, status=status.HTTP_201_CREATED)
