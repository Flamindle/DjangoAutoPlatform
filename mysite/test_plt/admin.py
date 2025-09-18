# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project



class ProjectAdmin(ModelAdmin):
    list_display = ['id','name','version','type','status','create_user','create_time','update_time']
    list_display_links = ['name','version']
    list_filter = ['create_time','type','create_user']
    search_fields = ['name','version']


# Register your models here.
# admin.site.register(Project, ProjectAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.site_header = "自动化测试后台管理系统"
admin.site.site_title = "Jacky自动化平台自研系统"
