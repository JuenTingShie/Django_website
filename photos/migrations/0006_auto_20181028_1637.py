# Generated by Django 2.1.2 on 2018-10-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20181028_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pho/%Y/%M/%D'),
        ),
    ]
