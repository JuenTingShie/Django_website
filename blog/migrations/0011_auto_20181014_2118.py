# Generated by Django 2.1.2 on 2018-10-14 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181014_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='which_post',
            new_name='post',
        ),
    ]