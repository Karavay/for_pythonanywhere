# Generated by Django 3.0.3 on 2020-03-21 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200319_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 15, 7, 2, 13850, tzinfo=utc), verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 15, 7, 1, 861716, tzinfo=utc), verbose_name='дата создания'),
        ),
    ]