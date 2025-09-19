# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project, ProjectMember


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

# 项目成员管理页面
class ProjectMemberAdmin(ModelAdmin):
    list_display = ('id', 'project', 'user','join_date','status')
    list_display_links = ('user', 'project')
    search_fields = ('user__first_name', 'user__username')
    list_filter = ('project','join_date','status')

admin.site.register(ProjectMember, ProjectMemberAdmin)