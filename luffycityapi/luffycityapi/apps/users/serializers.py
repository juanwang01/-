import re
from luffycityapi.luffycityapi.utils import constants
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# from rest_framework_jwt.settings import api_settings

from .models import User


class UserRegisterModelSerializer(serializers.ModelSerializer):
    """
    用户注册的序列化器
    """
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["mobile", "password", "re_password", "sms_code", "token"]
        extra_kwargs = {
            "mobile": {
                "required": True, "write_only": True
            },
            "password": {
                "required": True, "write_only": True, "min_length": 1, "max_length": 16,
            },
        }

    def validate(self, data):
        """验证客户端数据"""
        # 手机号格式验证
        mobile = data.get("mobile", None)
        if not re.match("^1[3-9]\d{9}$", mobile):
            raise serializers.ValidationError(detail="手机号格式不正确！", code="mobile")

        # 密码和确认密码
        password = data.get("password")
        re_password = data.get("re_password")
        if password != re_password:
            raise serializers.ValidationError(detail="密码和确认密码不一致！", code="password")

        # 手机号是否已注册
        try:
            User.objects.get(mobile=mobile)
            raise serializers.ValidationError(detail="手机号已注册！")
        except User.DoesNotExist:
            pass

        # todo 验证短信验证码

        return data

    def create(self, validated_data):
        """保存用户信息，完成注册"""
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")

        user = User.objects.create_user(
            username=mobile,
            mobile=mobile,
            avatar=constants.DEFAULT_USER_AVATAR,
            password=password,
        )


        # 使用 simplejwt 生成 JWT token
        refresh = RefreshToken.for_user(user)

        # 返回的 token 可以包含 access 和 refresh token
        user.token = str(refresh.access_token)

        return user