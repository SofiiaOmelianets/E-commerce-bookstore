# Generated by Django 3.0.6 on 2020-10-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201021_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.CharField(choices=[('Softcover', "М'яка обкладинка"), ('Hardcover', 'Тверда обкладинка')], max_length=9),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('UA', 'Українська'), ('RU', 'Російська'), ('EN', 'Англійська')], max_length=20),
        ),
    ]
