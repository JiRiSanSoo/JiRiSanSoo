# Generated by Django 3.2.7 on 2021-10-01 08:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0013_auto_20210930_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='위치', max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 1, 8, 30, 30, 679080, tzinfo=utc), verbose_name='data published'),
        ),
    ]
