# Generated by Django 3.0.6 on 2020-10-16 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20201016_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing',
            new_name='book',
        ),
    ]
