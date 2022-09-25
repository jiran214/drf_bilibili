from datetime import timedelta, datetime

from django.contrib.auth import get_user_model
from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserDetailSer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = User
        fields = ["name", "gender", "birthday", "email", "email", "image"]


class UserRegSer(serializers.ModelSerializer):
    """邮箱注册"""

    code = serializers.CharField(required=True,write_only=True,max_length=4, min_length=4, help_text="验证码",
                                 error_messages={
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 })
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    def validate(self, attrs):
        # 验证
        redis = get_redis_connection()
        if not redis.exists(attrs["username"]):
            raise serializers.ValidationError("请先获取验证码")
        code=redis.get(attrs["username"]).decode()
        input_code=attrs["code"]
        print('--------',code,input_code)
        if not (code == input_code):
            raise serializers.ValidationError("验证码错误")

        attrs["email"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ["username", "code", "email", "password"]

class EmailSer(serializers.Serializer):
    email = serializers.CharField(max_length=30)

    def validate_email(self, email):
        # 邮箱作为账号是否注册
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("用户已经存在")
        # 验证手机号码是否合法
        # if re.match(REGEX_MOBILE, email):
        # raise serializers.ValidationError("手机号码非法")
        # 验证发送频率

        redis = get_redis_connection()
        if redis.exists(email):
            raise serializers.ValidationError("请求频繁，请稍后重试")

        return email