# Generated by Django 3.2.6 on 2021-09-13 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitcategory',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='collection',
        ),
    ]