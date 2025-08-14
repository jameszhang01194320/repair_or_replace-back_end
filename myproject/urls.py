# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

def healthz(_):
    return JsonResponse({"ok": True})

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

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def signup_view(request):
    d = request.data
    username = d.get("username", "").strip()
    email = d.get("email", "").strip()
    first_name = d.get("first_name", "").strip()
    last_name = d.get("last_name", "").strip()
    password = d.get("password")
    password_confirm = d.get("password_confirm")

    if not username or not email or not password or not password_confirm:
        return Response({"message": "Required fields are missing."}, status=400)
    if password != password_confirm:
        return Response({"message": "Passwords do not match."}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"message": "Username already exists."}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({"message": "Email already exists."}, status=400)

    user = User.objects.create_user(
        username=username, email=email, password=password,
        first_name=first_name, last_name=last_name, is_active=True
    )
    # 如需注册后自动登录，可同时返回 token
    # token, _ = Token.objects.get_or_create(user=user)

    return Response(
        {"message": "Registration successful.", "user_id": user.id, "username": user.username},
        status=201,
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz/", healthz),
    path("api/login/", login_view),     # 你的 Login.jsx 用的
    path("api/signup/", signup_view),   # 你的 Register.jsx 用的
    path("api/", include("repair_management.urls")),  # 业务路由（有就保留）
]
