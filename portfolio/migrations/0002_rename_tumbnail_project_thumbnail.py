# Generated by Django 3.2.6 on 2021-08-19 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tumbnail',
            new_name='thumbnail',
        ),
    ]
