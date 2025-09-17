# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Project

# Register your models here.
# admin.site.register(Project, ProjectAdmin)
admin.site.register(Project)

admin.site.site_header = "自动化测试后台管理系统"
admin.site.site_title = "Jacky自动化平台自研系统"
