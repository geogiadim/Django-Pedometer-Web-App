# Generated by Django 3.1.7 on 2021-03-20 17:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pedometer', '0011_auto_20210320_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedometer',
            name='note',
        ),
        migrations.AlterField(
            model_name='pedometer',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 20, 17, 6, 7, 995319, tzinfo=utc)),
        ),
    ]
