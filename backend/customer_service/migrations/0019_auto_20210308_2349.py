# Generated by Django 3.1.3 on 2021-03-08 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_service', '0018_auto_20210302_0201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Автомобіль', 'verbose_name_plural': 'Автомобілі'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Клієнт', 'verbose_name_plural': 'Клієнти'},
        ),
        migrations.AlterField(
            model_name='car',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='car',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Країна'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(choices=[('Ф', 'Фізична особа'), ('Ю', 'Юридична особа')], default='Ф', max_length=1, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.AlterField(
            model_name='messagesmsinsurancepolicyexpires',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='messagesmsinsurancepolicyexpires',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='messagesmsinsurancepolicyexpires',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
    ]