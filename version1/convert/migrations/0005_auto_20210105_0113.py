# Generated by Django 3.1.4 on 2021-01-04 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0004_auto_20210103_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='created',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='updated',
        ),
    ]
