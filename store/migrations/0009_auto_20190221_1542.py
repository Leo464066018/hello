# Generated by Django 2.1 on 2019-02-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20190221_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='post_date',
            field=models.DateField(verbose_name='发货日期'),
        ),
    ]