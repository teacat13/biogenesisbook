# Generated by Django 3.0 on 2022-03-31 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biogenesis', '0007_auto_20220331_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='poster',
        ),
    ]
