# Generated by Django 3.2.9 on 2021-11-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_isbn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, max_length=260, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='format',
            field=models.CharField(blank=True, max_length=260, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]