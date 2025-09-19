#encoding: utf-8
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
#定义项目的model
class Project(models.Model):
    PROJECT_TYPE=(
        (1,'Web'),
        (2,'App'),
        (3,'PC'),
        (4,'接口'),
        (5,'功能'),
        (6,'性能'),
        (7,'安全'),
        (8,'硬件'),
        (9,'音频'),
        (10,'其它'),
    )
    #自增字段：主键id
    id = models.AutoField(primary_key=True)
    #项目名称
    name = models.CharField(max_length=200,verbose_name='测试项目')
    #项目版本：
    version = models.CharField(max_length=100,default='1.0',verbose_name='项目版本')
    #项目类型
    type = models.IntegerField(choices=PROJECT_TYPE,default=1,verbose_name='项目类型')
    #项目描述
    describe = models.TextField(max_length=200,null=True,blank=True,verbose_name='项目描述')
    #项目状态
    status=models.BooleanField(default=True,verbose_name='项目状态')
    #创建人
    create_user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name='创建人')
    #创建时间
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    #最后更新时间
    update_time=models.DateTimeField(auto_now=True,verbose_name='最后更新时间')
    #默认显示
    def __str__(self):
        return self.name

    #项目描述：内部类
    class Meta:
        #给人看的
        verbose_name = '自动化测试'
        verbose_name_plural = "测试项目"