# Generated by Django 3.0.6 on 2020-05-21 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0008_auto_20200521_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tagname',
            new_name='name',
        ),
    ]