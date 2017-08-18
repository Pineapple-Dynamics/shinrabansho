from django.db import models
from datetime import datetime

# Create your models here.

class web_app_data(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)

class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    #レコード名
    def __str__(self):
        return self.name
