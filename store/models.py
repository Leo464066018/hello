from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    CHOICES = (('YZ', '扬州'), ('BJ', '北京'), ('CQ', '重庆'))

    name = models.CharField(max_length=30, verbose_name='配件名')
    qty = models.IntegerField(verbose_name='数量')
    city = models.CharField(max_length=8, choices=CHOICES, verbose_name='城市')
    who_does = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='操作人')
    note = models.CharField(max_length=128, verbose_name='备注')
    modify_date = models.DateTimeField(auto_now=True, verbose_name='修改日期')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '配件库'


class Operation(models.Model):
    OPERATIONS = (('plus', '增加'), ('minus', '减少'))

    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, verbose_name='配件')
    operate = models.CharField(max_length=8, choices=OPERATIONS, verbose_name='操作')
    num = models.IntegerField(verbose_name='数目')
    operated_time = models.DateTimeField(auto_now_add=True, verbose_name='操作日期')

    def __str__(self):
        return self.item

    class Meta:
        verbose_name_plural = '操作记录'

