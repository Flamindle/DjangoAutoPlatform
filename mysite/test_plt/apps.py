#encoding: utf-8
from django.apps import AppConfig


class TestPltConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #给程序看的
    name = 'test_plt'
    #给人看的
    verbose_name='测试平台（探索模块，不使用）'
