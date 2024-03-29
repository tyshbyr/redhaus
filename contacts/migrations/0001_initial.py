# Generated by Django 3.2.6 on 2021-09-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallBackOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('time_to_call', models.CharField(max_length=50, verbose_name='Удобное время звонка')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Обратный звонок',
                'verbose_name_plural': 'Обратные звонки',
            },
        ),
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('mail', models.CharField(max_length=50, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('site', models.CharField(max_length=50, verbose_name='Сайт')),
                ('company', models.CharField(max_length=50, verbose_name='Компания')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заявка на сотрудничество',
                'verbose_name_plural': 'Заявки на сотрудничество',
            },
        ),
        migrations.CreateModel(
            name='CustomerQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Телефон')),
                ('mail', models.CharField(max_length=50, verbose_name='Электронная почта')),
                ('question', models.TextField(max_length=50, verbose_name='Вопрос посетителя')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('comment', models.TextField(max_length=50, verbose_name='Комментарий')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заявка на заказ',
                'verbose_name_plural': 'Заявки на заказ',
            },
        ),
    ]
