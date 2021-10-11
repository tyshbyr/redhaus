from django.db import models

# Create your models here.

class CallBackOrder(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    time_to_call = models.CharField(max_length=50, verbose_name='Удобное время звонка')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'


class CustomerQuestion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    mail = models.CharField(max_length=50, verbose_name='Электронная почта')
    question = models.TextField(max_length=50, verbose_name='Вопрос посетителя')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'



class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(max_length=50, verbose_name='Комментарий')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на заказ'
        verbose_name_plural = 'Заявки на заказ'


class Cooperation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    city = models.CharField(max_length=50, verbose_name='Город')
    mail = models.CharField(max_length=50, verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    company = models.CharField(max_length=50, verbose_name='Компания')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на сотрудничество'
        verbose_name_plural = 'Заявки на сотрудничество'
