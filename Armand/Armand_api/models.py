from django.db import models

# Create your models here.

class DB_notify(models.Model):
    content = models.CharField(max_length=100, null=True, blank=True, default='')

    def __str__(self):
        return self.content
