# Generated by Django 3.2.6 on 2021-09-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210913_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=16, on_delete=django.db.models.deletion.PROTECT, to='catalog.productcategory', verbose_name='Категория изделия'),
            preserve_default=False,
        ),
    ]
