from django.db import models
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    slug = models.SlugField(max_length=100, unique = True, db_index=True, verbose_name='Url')
    date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    short_description = models.CharField(max_length=200, verbose_name='Короткое описание')
    thumbnail = models.ImageField(upload_to='cache/news_index/images/upload/', verbose_name='Изображение')
    description = models.TextField(max_length=200, verbose_name='Описание')
    to_publish = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Gallery(models.Model):
    image = models.ImageField(upload_to='cache/news_show/images/upload/', verbose_name='Изображение')
    binding = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Фотографии')

    def __str__(self):
        return str(self.binding)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'