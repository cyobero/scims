# Generated by Django 3.1.7 on 2021-05-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productstock_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]