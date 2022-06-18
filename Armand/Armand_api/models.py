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


# table:项目列表
class DB_proj_list(models.Model):
    proj_name = models.CharField(max_length=100, null=True, blank=True, default='-')
    des = models.CharField(max_length=500, null=True, blank=True, default='-')
    creator = models.IntegerField(default=0)
    updator = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 更新时间

    def __str__(self):
        return self.proj_name