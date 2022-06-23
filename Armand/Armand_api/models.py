from django.db import models

# Create your models here.

class DB_notify(models.Model):
    content = models.CharField(max_length=100, null=True, blank=True, default='')

    def __str__(self):
        return self.content

class DB_news(models.Model):
    from_user_id = models.IntegerField(default=0)
    to_user_id = models.IntegerField(default=0)
    content = models.CharField(max_length=500, null=True, blank=True, default='-')

    def __str__(self):
        return self.content[:20]+'...'


# table:项目基本信息
class DB_proj_list(models.Model):
    proj_name = models.CharField(max_length=100, null=True, blank=True, default='-')
    des = models.CharField(max_length=500, null=True, blank=True, default='-')
    creator = models.IntegerField(default=0)
    updator = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 更新时间
    mock_type = models.CharField(max_length=50, null=True, blank=True, default='mock_data')  # mock类型 value: mock_data, mock_3rd
    private = models.BooleanField(default=False)  # 是否是私密项目
    Group = models.CharField(max_length=200, null=True, blank=True, default='')  # 测试组: System Testing, Terminal Testing
    Logon_var = models.CharField(max_length=500, null=True, blank=True, default='')  # 登录态变量
    Public_var = models.CharField(max_length=500, null=True, blank=True, default='')  # 公共变量
    Permission = models.CharField(max_length=500, null=True, blank=True, default='[]')  # 权限 value: me,teammates, leader, all
    sign = models.CharField(max_length=500, null=True, blank=True, default='')  # 加密算法
    hide_flag = models.BooleanField(default=False)  # fake delete

    def __str__(self):
        return self.proj_name