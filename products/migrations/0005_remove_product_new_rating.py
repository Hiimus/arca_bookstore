# Generated by Django 3.2.9 on 2021-12-22 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211222_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='new_rating',
        ),
    ]
