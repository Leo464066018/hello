# Generated by Django 2.1 on 2019-02-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20190221_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='note',
            field=models.CharField(default=0, max_length=128, verbose_name='备注'),
            preserve_default=False,
        ),
    ]
