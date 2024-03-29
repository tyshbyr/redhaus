# Generated by Django 3.2.6 on 2021-09-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kit',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalog.kitcategory', verbose_name='Категория комплекта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.productcategory', verbose_name='Категория изделия'),
        ),
    ]
