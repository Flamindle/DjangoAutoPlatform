#encoding: utf-8
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
#定义项目的model
class Project(models.Model):
    #项目类型
    PROJECT_TYPE = (
        (1, 'web'),
        (2, 'app'),
        (3, '接口'),
        (4, '功能'),
        (5, '性能'),
        (6, '安全'),
        (7, '硬件'),
        (8, '其他')
    )

    #自增字段：主键id
    id = models.AutoField(primary_key=True)
    #项目名称
    name = models.CharField(max_length=100,verbose_name='Jacky测试项目')

    #版本
    version = models.CharField(max_length=50,verbose_name='版本')
    #类型
    type = models.IntegerField(choices=PROJECT_TYPE,default=1,verbose_name='产品类型')

    #描述
    describe = models.TextField(max_length=200,blank=True,null=True,verbose_name='项目描述')

    #状态
    status = models.BooleanField(default=True,verbose_name='状态')

    #创建人:外键
    create_user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name='创建人')

    #创建时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    #最后更新时间
    update_time = models.DateTimeField(auto_now=True,verbose_name='最后更新时间')

    #项目成员TODO

    #测试环境TODO

    #默认显示
    def __str__(self):
        return self.name

    #项目描述：内部类
    class Meta:
        #给人看的
        verbose_name = '自动化测试'
        verbose_name_plural = verbose_name