#encoding: utf-8
from django.apps import AppConfig


class TestPltConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #给程序看的
    name = 'auto_test_plt'
    #给人看的
    verbose_name='自动化测试平台'
