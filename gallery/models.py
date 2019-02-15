from django.db import models

# Create your models here.
# 1、创建model，2、去admin.py注册model


class Gallery(models.Model):
    description = models.CharField(default='在此处填写作品简介', max_length=100)
    image = models.ImageField(default='default.png', upload_to='image/')
    title = models.CharField(default='标题', max_length=50)

    def __str__(self):
        return self.title

