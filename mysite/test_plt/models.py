#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ctypes.wintypes import PCHAR


class Project(models.Model):
    TESTING_TYPE = (
        (1, 'Web'),
        (2, 'App'),
        (3, 'PC'),
        (4, '接口'),
        (5, '功能'),
        (6, '性能'),
        (7, '安全'),
        (8, '硬件'),
        (9, '音频'),
        (10, '其它'),
    )

    # 1. 主键，自增
    id = models.AutoField(primary_key=True, verbose_name="主键")

    # 2. 缺陷标题（数据库限制 100 字，默认 " "）
    title = models.CharField(max_length=100, default=" ", verbose_name="缺陷标题")

    # 3. 摘要
    summary = models.TextField(default=" ", verbose_name="摘要")

    # 4. 复现步骤
    recovery = models.TextField(default=" ", verbose_name="复现步骤")

    # 5. 前置条件
    precondition = models.TextField(default=" ", verbose_name="前置条件")

    # 6. 操作步骤
    step = models.TextField(default=" ", verbose_name="操作步骤")

    # 7. 预期结果
    expect = models.TextField(max_length=200, default=" ", verbose_name="预期结果")

    # 8. 实际结果
    actual = models.TextField(max_length=200, default=" ", verbose_name="实际结果")

    # 9. 复现概率
    repro = models.CharField(max_length=100, default=" ", verbose_name="复现概率")

    # 10. 配置信息
    config = models.TextField(default=" ", verbose_name="配置信息")

    # 11. 蓝牙地址
    bt_address = models.TextField(max_length=100, default=" ", verbose_name="蓝牙地址")

    # 12. 回归测试
    regression = models.TextField(default=" ", verbose_name="回归测试")

    # 13. 备注
    note = models.TextField(max_length=200, default=" ", verbose_name="备注")

    # 14. 时间戳（存字符串，但建议用 IntegerField 存 Unix 时间戳）
    timestamp = models.TextField(max_length=100, default=" ", verbose_name="时间戳")

    # 15. 提交人（下拉框 → 关联 User）
    reporter = models.ForeignKey(
        User,
        related_name="reported_projects",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="提交人"
    )

    # 16. 评审人（下拉框 → 关联 User）
    reviewer = models.ForeignKey(
        User,
        related_name="reviewed_projects",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="评审人"
    )

    # 17. 日期
    date = models.DateField(default=timezone.now, verbose_name="日期")

    # 18. 测试类型
    test_type = models.IntegerField(choices=TESTING_TYPE, default=1, verbose_name="测试类型")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "缺陷管理"
        verbose_name_plural = verbose_name
