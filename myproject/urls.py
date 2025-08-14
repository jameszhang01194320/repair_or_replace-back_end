# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# 可选：健康检查
def healthz(_):
    return JsonResponse({"ok": True})

# 登录：前端仍然请求 /api/login/，返回 { token, user_id, username }
@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"message": "Username and password required."}, status=400)
    user = authenticate(username=username, password=password)
    if user is None or not user.is_active:
        return Response({"message": "Invalid username or password."}, status=400)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user_id": user.id, "username": user.username})

# 注册：前端请求 /api/signup/（你 Register.jsx 里已经写好了）
@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def signup_view(request):
    data = request.data
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    password = data.get("password")
    password_confirm = data.get("password_confirm")  # 你的前端就是这个字段名

    # 基本校验
    if not username or not email or not password or not password_confirm:
        return Response({"message": "Required fields are missing."}, status=400)
    if password != password_confirm:
        return Response({"message": "Passwords do not match."}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"message": "Username already exists."}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({"message": "Email already exists."}, status=400)

    # 创建用户
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        is_active=True,
    )

    # 可选：立即生成 token（如果你想注册后直接登录，可以把它返回给前端）
    token, _ = Token.objects.get_or_create(user=user)

    return Response(
        {
            "message": "Registration successful.",
            "user_id": user.id,
            "username": user.username,
            # "token": token.key,  # 若注册后要自动登录可打开，并在前端保存
        },
        status=201,
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz/", healthz),
    path("api/login/", login_view),      # ← 和你旧前端保持一致
    path("api/signup/", signup_view),    # ← 对应 Register.jsx
    path("api/", include("repair_management.urls")),  # 有业务路由就保留，没有可去掉
    path("api-auth/", include("rest_framework.urls")),  # 可选
]
