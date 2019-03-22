from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Box(models.Model):
    box_id = models.CharField(max_length=8, verbose_name="设备ID")
    sim_card = models.CharField(max_length=13, verbose_name="sim卡号")

    def __str__(self):
        return self.box_id

    class Meta:
        verbose_name = "sim卡"
        verbose_name_plural = verbose_name


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
        verbose_name = "配件"
        verbose_name_plural = verbose_name 
        ordering=['qty']


class Operation(models.Model):
    OPERATIONS = (('plus', '增加'), ('minus', '减少'))
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, verbose_name='配件')
    operate = models.CharField(max_length=8, choices=OPERATIONS, verbose_name='操作')
    num = models.IntegerField(verbose_name='数目')
    operated_time = models.DateTimeField(auto_now_add=True, verbose_name='操作日期')
    note = models.CharField(max_length=128, verbose_name='备注')

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = '操作记录'
        verbose_name_plural = verbose_name
        ordering = ('-operated_time',)


class PostManage(models.Model):
    SERVERTYPES = (('wifi', 'wifi服务器'), ('video', '视频服务器'))
    SENDORRECEIVE = (('send', '发货'), ('receive', '回收'))
    post_num = models.IntegerField(verbose_name='单号')
    post_date = models.DateField(verbose_name='发货日期')
    post_type = models.CharField(max_length=8, choices=SENDORRECEIVE, default='send', verbose_name='收寄类型')
    server_type = models.CharField(max_length=20, choices=SERVERTYPES, verbose_name='型号')
    server_num = models.IntegerField(verbose_name='数量')
    note_text = models.CharField(max_length=128, verbose_name='备注')

    class Meta:
        verbose_name = '发货记录'
        verbose_name_plural = verbose_name
        ordering = ('-post_date',)
