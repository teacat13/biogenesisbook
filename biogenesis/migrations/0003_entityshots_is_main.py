# Generated by Django 4.0.3 on 2022-03-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biogenesis', '0002_alter_entityshots_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='entityshots',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Главная картинка'),
        ),
    ]