#encoding: utf-8
from django.apps import AppConfig


class IssueManagePltConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "issue_manage_plt"
    #给人看的
    verbose_name='缺陷管理平台'