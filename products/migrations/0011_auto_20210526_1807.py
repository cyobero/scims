# Generated by Django 3.1.7 on 2021-05-26 18:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210526_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resin',
            fields=[
                ('flower_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.flower')),
            ],
            bases=('products.flower',),
        ),
        migrations.RemoveField(
            model_name='edible',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='edible',
            name='thc_content',
        ),
        migrations.AddField(
            model_name='flower',
            name='cbd_content',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='CBD Content (%)'),
        ),
        migrations.AddField(
            model_name='flower',
            name='final_test_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flower',
            name='harvest_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flower',
            name='package_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='net_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='flower',
            name='flower_type',
            field=models.CharField(blank=True, choices=[('I', 'Indica'), ('S', 'Sativa'), ('H', 'Hybrid')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='flower',
            name='thc_content',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='THC Content (%)'),
        ),
        migrations.DeleteModel(
            name='ProductStock',
        ),
    ]