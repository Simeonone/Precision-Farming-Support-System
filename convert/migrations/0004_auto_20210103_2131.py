# Generated by Django 3.1.4 on 2021-01-03 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0003_auto_20210103_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='image2',
            new_name='image',
        ),
    ]
