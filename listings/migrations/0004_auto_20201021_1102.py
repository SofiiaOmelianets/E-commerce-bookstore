# Generated by Django 3.0.6 on 2020-10-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200920_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='annotation',
        ),
        migrations.AddField(
            model_name='book',
            name='can_be_exchanged',
            field=models.BooleanField(default=False),
        ),
    ]
