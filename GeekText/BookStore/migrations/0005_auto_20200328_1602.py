# Generated by Django 2.2 on 2020-03-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0004_auto_20200328_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5),
        ),
    ]
