from django.db import models

# Create your models here.
"""
1. 定义模型
2. 模型迁移
3. 操作数据库
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo)
