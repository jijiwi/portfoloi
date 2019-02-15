from django.db import models

# Create your models here.

# 1、创建model，2、去admin.py注册model
class Gallery(models.Model):
    description = models.CharField(max_length=100)
