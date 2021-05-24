# Generated by Django 3.1.7 on 2021-05-24 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210524_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='productstock',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstock',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
