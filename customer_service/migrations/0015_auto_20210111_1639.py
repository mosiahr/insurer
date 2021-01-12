# Generated by Django 3.1.3 on 2021-01-11 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0014_auto_20210108_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 14, 39, 2, 495565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 14, 39, 2, 495565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 14, 39, 2, 495565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 14, 39, 2, 495565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagesmsinsurancepolicyexpires',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 14, 39, 2, 495565, tzinfo=utc)),
        ),
    ]
