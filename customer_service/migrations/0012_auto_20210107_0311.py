# Generated by Django 3.1.3 on 2021-01-07 01:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0011_auto_20210106_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageSmsInsurancePolicyExpires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sid', models.CharField(max_length=200)),
                ('body', models.TextField(verbose_name='Message body')),
                ('from_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('to_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer_service.car', verbose_name='Car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer_service.customer', verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Message SMS',
                'verbose_name_plural': 'Messages SMS',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='insurancepolicy',
            name='sms',
        ),
        migrations.DeleteModel(
            name='MessageSms',
        ),
        migrations.AddField(
            model_name='messagesmsinsurancepolicyexpires',
            name='insurance_policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer_service.insurancepolicy', verbose_name='Insurance Policy'),
        ),
    ]