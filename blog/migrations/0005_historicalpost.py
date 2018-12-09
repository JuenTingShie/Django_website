# Generated by Django 2.1.3 on 2018-12-09 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20181209_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPost',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('author', models.CharField(editable=False, max_length=200, verbose_name='作者')),
                ('title', models.CharField(max_length=200, verbose_name='標題')),
                ('slug', models.SlugField(editable=False, verbose_name='網址')),
                ('context', models.TextField(verbose_name='文章內容')),
                ('publish_time', models.DateTimeField(blank=True, editable=False, verbose_name='發布時間')),
                ('edited_time', models.DateTimeField(blank=True, editable=False, verbose_name='修改時間')),
                ('image', models.TextField(blank=True, max_length=100, verbose_name='側邊圖片')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical post',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
