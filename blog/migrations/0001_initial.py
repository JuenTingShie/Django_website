# Generated by Django 2.1.3 on 2018-11-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='標題')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='網址')),
                ('context', models.TextField(verbose_name='文章內容')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='發布時間')),
                ('edited_time', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
            ],
        ),
    ]
