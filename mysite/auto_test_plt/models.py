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

class ProjectMember(models.Model):
    '''
    项目成员:项目与用户的关系
    '''
    MEMBER_ROLE=(
        (1,'测试工程师'),
        (2,'测试组长'),
        (3,'测试经理'),
        (4,'开发工程师'),
        (5,'运维工程师'),
        (6,'项目经理'),
    )

    id=models.AutoField(primary_key=True, verbose_name="主键")
    project=models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="测试项目")
    # user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True, verbose_name="用户")
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="auto_members",  # 👈 改成唯一名字
        verbose_name="用户"
    )
    join_date=models.DateField(verbose_name="加入日期")
    role=models.IntegerField(choices=MEMBER_ROLE, verbose_name="角色")
    status=models.BooleanField(default=True, verbose_name="状态")
    quit_date=models.DateField(verbose_name="退出日期",null=True, blank=True)
    memo=models.TextField(max_length=200, default=" ", verbose_name="备注", null=True, blank=True)

    def __str__(self):
        if not self.user:
            return "-"
        else:
            first_name=self.user.first_name if self.user.first_name else "-"
            username=self.user.username

            return f"{first_name}({username})"

    class Meta:
        verbose_name = "项目成员"
        verbose_name_plural = verbose_name