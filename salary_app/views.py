from django.shortcuts import render, reverse
from .models import Salary
from django.http import HttpResponseRedirect, Http404
from .form import SalaryFrom
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'salary_app/index.html')


@login_required
def salaries(request):
    """显示所有的工资"""
    salaries = Salary.objects.filter(owner=request.user).order_by("date_added")
    context = {"salaries": salaries}
    return render(request, "salary_app/salaries.html", context)


@login_required
def salary(request, salary_id):
    """显示单条工资"""
    salary = Salary.objects.get(id=salary_id)
    # 确认请求的主题属于当前用户
    if salary.owner != request.user:
        raise Http404
    context = {"salary": salary}
    return render(request, "salary_app/salary.html", context)


@login_required
def new_salary(request):
    """添加工资明细"""
    if request.method != "POST":
        form = SalaryFrom()
    else:
        form = SalaryFrom(request.POST)
        if form.is_valid():
            new_salary = form.save(commit=False)
            new_salary.owner = request.user
            new_salary.save()
            return HttpResponseRedirect(reverse("salary_app:salaries"))
    context = {"form": form}
    return render(request, "salary_app/new_salary.html", context)


@login_required
def edit_salary(request, salary_id):
    """编辑工资明细"""
    salary = Salary.objects.get(id=salary_id)
    # 确认请求的主题属于当前用户
    if salary.owner != request.user:
        raise Http404
    if request.method != "POST":
        form = SalaryFrom(instance=salary)
    else:
        form = SalaryFrom(instance=salary, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("salary_app:salary", args=[salary.id]))
    context = {"salary": salary, "form": form}
    return render(request, "salary_app/edit_salary.html", context)


@login_required
def delete_salary(request, salary_id):
    """删除工资明细"""
    salary = Salary.objects.get(id=salary_id)
    salary.delete()
    return HttpResponseRedirect(reverse("salary_app:salaries"))
