# Generated by Django 3.2.9 on 2021-12-22 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_ratings', to='products.review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to='products.product'),
        ),
    ]