#encoding: utf-8
from django.db import models


# Create your models here.
#定义项目的model
class Project(models.Model):
    #自增字段：主键id
    id = models.AutoField(primary_key=True)
    #项目名称
    name = models.CharField(max_length=200,verbose_name='测试项目')

    #默认显示
    def __str__(self):
        return self.name

    #项目描述：内部类
    class Meta:
        #给人看的
        verbose_name = '自动化测试'
        verbose_name_plural = "自动化测试项目"