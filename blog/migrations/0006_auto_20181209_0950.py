# Generated by Django 2.1.3 on 2018-12-09 01:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_historicalpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpost',
            name='history_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
