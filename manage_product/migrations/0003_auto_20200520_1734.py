# Generated by Django 3.0.6 on 2020-05-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0002_auto_20200520_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
