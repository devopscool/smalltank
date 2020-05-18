# Generated by Django 2.2.8 on 2020-05-18 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200518_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='content',
            field=models.TextField(blank=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 18, 9, 56, 45, 417676), verbose_name='last update date'),
        ),
    ]
