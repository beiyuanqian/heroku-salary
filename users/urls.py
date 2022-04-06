# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/4/2}

"""定义users的URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
]
