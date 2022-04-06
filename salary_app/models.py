from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Salary(models.Model):
    """工资明细"""
    year = models.CharField("年份", max_length=100)
    month = models.CharField("月份", max_length=100)
    attendance_day = models.CharField("出勤天数", max_length=100)
    base_pay = models.CharField("基本工资", max_length=100)
    post_way = models.CharField("岗位工资", max_length=100)
    merit_pay = models.CharField("绩效工资", max_length=100)
    benefit_bonus = models.CharField("效益奖", max_length=100)
    seniority_pay = models.CharField("工龄工资", max_length=100)
    overtime_wage = models.CharField("加班工资", max_length=100)
    wage_subtotal = models.CharField("工资小计", max_length=100)

    meal_subsidy = models.CharField("餐费补贴", max_length=100)
    high_temperature_subsidy = models.CharField("高温补贴", max_length=100)
    housing_allowance = models.CharField("住房补贴", max_length=100)
    traffic_subsidy = models.CharField("交通补贴", max_length=100)
    health_care_subsidy = models.CharField("保健补贴", max_length=100)
    middle_night_subsidy = models.CharField("中晚班津贴", max_length=100)
    scarce_specialty_subsidy = models.CharField("稀缺专业补贴", max_length=100)
    subsidy_subtotal = models.CharField("补贴小计", max_length=100)

    meals_deduction = models.CharField("餐费扣款", max_length=100)
    rent_deduction = models.CharField("房租扣款", max_length=100)
    water_electricity_deduction = models.CharField("水电扣款", max_length=100)
    sunshine_due = models.CharField("阳光会费", max_length=100)
    social_security = models.CharField("社保扣款", max_length=100)
    accumulation_fund = models.CharField("公积金", max_length=100)
    income_tax = models.CharField("所得税", max_length=100)
    deduction_subtotal = models.CharField("扣款小计", max_length=100)

    net_pay = models.CharField("应发工资", max_length=100)
    net_payroll = models.CharField("实发工资", max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回字符的字符串表示"""
        return self.year + "-" + self.month
