# Generated by Django 3.0 on 2022-05-11 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biogenesis', '0015_auto_20220511_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='Book',
            new_name='book',
        ),
    ]
