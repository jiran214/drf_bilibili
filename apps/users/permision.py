from rest_framework.permissions import BasePermission


class VipPermission(BasePermission):
    message = '只有VIP才能访问'  # 错误提示 系统会自动调用  通过反射

    def has_permission(self, request, view):
        # 判断是否已经通过认证  通过 request.auth 判断 认证成功后保存的token 参数
        #  如果没有 认证  request.user  也是空的  下面的操作就会报错
        if not request.auth:
            return False
        # 如果你是VIP才有权限访问
        # request.user:当前经过认证的用户对象
        print(request.user.vip)
        if request.user.vip:
            return True
        else:
            # 如果不是VIP就拒绝范围跟
            return False