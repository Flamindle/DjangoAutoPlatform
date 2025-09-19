# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    # 列表页显示字段
    list_display = ['id', 'name', 'type','status','version','create_time', 'update_time']

    # 搜索框
    search_fields = ['name']

    # 右侧过滤器
    list_filter = ['create_time', 'type','describe']



admin.site.register(Project,ProjectAdmin)

admin.site.site_header = "测试管理系统"
admin.site.site_title = "Jacky自动化平台自研系统"
