# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project, ProjectMember, DeployEnv

#**************************内联页面**************************
class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember
    extra = 2

class DeployEnvInline(admin.TabularInline):
    model = DeployEnv
    extra = 2
# admin.site.register(ProjectMemberInline)

#**************************测试项目页面**************************
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # 列表页显示字段
    list_display = ['id', 'name', 'type','status','version','create_time', 'update_time']
    # 搜索框
    search_fields = ['name']
    # 右侧过滤器
    list_filter = ['create_time', 'type','describe']
    # 链接到详情页
    list_display_links = ['name']
    #内联的model
    inlines=[ProjectMemberInline,DeployEnvInline]

    # fields = ('name', ('version','type'),('create_user','status'),'describe')
    fieldsets = (
        ('基本信息',{
            'fields':(('name' ,'status'),('version','type'),'create_user')
        }),
        ('描述信息',{
            'classes':('collapse',),
            'fields':('describe',)
        })
    )
# admin.site.register(Project,ProjectAdmin)

#**************************项目成员页面**************************
@admin.register(ProjectMember)
class ProjectMemberAdmin(ModelAdmin):
    list_display = ['id', 'project', 'user','join_date','status']
    list_display_links = ['user', 'project']
    search_fields = ['user__first_name', 'user__username']
    list_filter = ['project','join_date','status']

# admin.site.register(ProjectMember, ProjectMemberAdmin)

#**************************测试环境页面**************************
@admin.register(DeployEnv)
class DeployEnvAdmin(ModelAdmin):
    list_display = ['id', 'project', 'name','hostname','port','status']
    list_display_links = ['name']
    search_fields = ['name', 'hostname']
    list_filter = ['project','status']

# admin.site.register(DeployEnv, DeployEnvAdmin)

#**************************总标题**************************
admin.site.site_header = "测试管理系统"
admin.site.site_title = "Jacky自动化平台自研系统"
