# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Project


# 自定义表单，调整输入框大小
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            # CharField 输入框调长一些，方便输入
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 80}),
            'repro': forms.Textarea(attrs={'rows': 1, 'cols': 30}),

            # TextField 默认 textarea，可以调节行列
            'summary': forms.Textarea(attrs={'rows': 5, 'cols': 80}),
            'recovery': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'precondition': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'step': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'config': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'bt_address': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'regression': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'expect': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'actual': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
        }


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

    # 列表页显示字段
    list_display = ('id', 'title', 'reporter', 'reviewer', 'date')

    # 搜索框
    search_fields = ('title', 'summary', 'reporter__username', 'reviewer__username')

    # 右侧过滤器
    list_filter = ('date', 'reporter', 'reviewer')


# 传统注册方法
admin.site.register(Project, ProjectAdmin)

# # 设置后台标题
# admin.site.site_header = "缺陷管理系统"
# admin.site.site_title = "Jacky自动化平台自研系统"

