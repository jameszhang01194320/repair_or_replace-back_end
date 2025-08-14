# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token

# 简单健康检查，用于 Render Health Check（可选）
def healthz(_request):
    return JsonResponse({"ok": True})

urlpatterns = [
    # Django 后台
    path("admin/", admin.site.urls),

    # DRF Token 登录端点：POST { "username": "...", "password": "..." } -> { "token": "..." }
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    # 健康检查（Render -> Settings -> Health Check Path 可填 /healthz）
    path("healthz/", healthz),

    # 如果你的业务 app 有 urls.py，就挂到 /api/ 下；如果没有，此行可先删掉
    path("api/", include("repair_management.urls")),

    # （可选）DRF 浏览器调试登录页
    path("api-auth/", include("rest_framework.urls")),
]
