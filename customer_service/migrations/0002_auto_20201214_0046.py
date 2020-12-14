# Generated by Django 3.1.3 on 2020-12-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancepolicy',
            name='is_called_will_insure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='is_called_will_not_insure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='is_impossible_to_call',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='is_reinsured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='is_reinsured_another_company',
            field=models.BooleanField(default=False),
        ),
    ]
