# Generated by Django 2.2 on 2020-03-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0003_auto_20200327_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=5),
        ),
    ]
