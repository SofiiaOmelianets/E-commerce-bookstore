# Generated by Django 3.0.6 on 2020-10-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20201021_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.CharField(choices=[("М'яка обкладинка", "М'яка обкладинка"), ('Тверда обкладинка', 'Тверда обкладинка')], max_length=20),
        ),
    ]
