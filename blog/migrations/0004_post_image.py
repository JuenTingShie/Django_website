# Generated by Django 2.1.2 on 2018-10-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181011_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=200, verbose_name='圖片'),
        ),
    ]
