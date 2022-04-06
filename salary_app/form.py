# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/4/2}

from django import forms
from .models import Salary


class SalaryFrom(forms.ModelForm):
    class Meta:
        model = Salary
        fields='__all__'
