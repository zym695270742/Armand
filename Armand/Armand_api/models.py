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
