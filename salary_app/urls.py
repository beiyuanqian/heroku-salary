# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/4/1}

"""定义salary_app的URL模式"""
from django.urls import path
from . import views

app_name = 'salary_app'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path("salaries/", views.salaries, name="salaries"),
    path('salaries/<int:salary_id>/', views.salary, name="salary"),
    path("new_salary/", views.new_salary, name="new_salary"),
    path("edit_salary/<int:salary_id>", views.edit_salary, name="edit_salary"),
    path("delete_salary/<int:salary_id>",views.delete_salary,name="delete_salary")
]
