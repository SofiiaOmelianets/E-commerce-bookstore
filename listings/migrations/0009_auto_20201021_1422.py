# Generated by Django 3.0.6 on 2020-10-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20201021_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
    ]