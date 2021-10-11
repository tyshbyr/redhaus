from django.db import models
from django.urls import reverse


# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название коллекции')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'



class KitCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique = True, db_index=True, verbose_name='Url')
    short_description = models.CharField(max_length=100, verbose_name='Короткое описание', blank=True)
    thumbnail = models.ImageField(upload_to='cache/catalog_list/images/upload/', verbose_name='Изображение')
    price = models.CharField(max_length=100, verbose_name='Цена', blank=True)
    to_publish = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория комплектов'
        verbose_name_plural = 'Категории комплектов'



class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique = True, db_index=True, verbose_name='Url')
    short_description = models.CharField(max_length=100, verbose_name='Короткое описание', blank=True)
    thumbnail = models.ImageField(upload_to='cache/catalog_list/images/upload/', verbose_name='Изображение')
    price = models.CharField(max_length=100, verbose_name='Цена', blank=True)
    to_publish = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория изделий'
        verbose_name_plural = 'Категории изделий'


class Kit(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Коллекция')
    category = models.ForeignKey(KitCategory, on_delete=models.PROTECT, verbose_name='Категория комплекта')
    slug = models.SlugField(max_length=100, unique = True, db_index=True, verbose_name='Url')
    title = models.CharField(max_length=100, verbose_name='Название комплекта')
    thumbnail = models.ImageField(upload_to='cache/catalog_list/images/upload/', verbose_name='Миниатюра комплекта')
    short_description = models.CharField(max_length=100, verbose_name='Короткое описание', blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    info = models.TextField(verbose_name='Информация', null=True, blank=True)
    price = models.CharField(max_length=100, verbose_name='Цена', blank=True)
    to_publish = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:kit_page', kwargs={'kit_slug':self.slug})

    class Meta:
        verbose_name = 'Комплект'
        verbose_name_plural = 'Комплекты'
        ordering = ['-id']

class SliderKit(models.Model):
    image = models.ImageField(upload_to='cache/catalog_slider/images/upload/', verbose_name='Путь к файлу изображения')
    binding = models.ForeignKey(Kit, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Комплект')

    def __str__(self):
        return str(self.binding)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

class ColorKit(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название цвета')
    image = models.ImageField(upload_to='cache/catalog_color/images/upload/', verbose_name='Изображение цвета')
    render = models.ImageField(upload_to='cache/catalog_color_render/images/upload/', blank=True, verbose_name='Рендер цвета')
    recommended = models.BooleanField(default=True, verbose_name='Рекомендуемый цвет')
    binding = models.ForeignKey(Kit, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Цвет комплекта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета комплекта'



class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Коллекция')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='Категория изделия')
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Комплект изделия')
    title = models.CharField(max_length=100, verbose_name='Название изделия')
    slug = models.SlugField(max_length=100, unique = True, db_index=True, verbose_name='Url')
    short_description = models.CharField(max_length=100, verbose_name='Короткое описание', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    info = models.TextField(verbose_name='Информация', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='cache/catalog_list/images/upload/', verbose_name='Миниатюра изображения')
    price = models.CharField(max_length=100, verbose_name='Цена', null=True, blank=True)
    to_publish = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:product_page', kwargs={'product_slug':self.slug})

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'

class SliderProduct(models.Model):
    image = models.ImageField(upload_to='cache/catalog_slider/images/upload/', verbose_name='Путь к файлу изображения')
    binding = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Изображения изделия')

    def __str__(self):
        return str(self.binding)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

class ColorProduct(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название цвета')
    image = models.ImageField(upload_to='cache/catalog_color/images/upload/', verbose_name='Изображение цвета')
    render = models.ImageField(upload_to='cache/catalog_color_render/images/upload/', blank=True, verbose_name='Рендер цвета')
    recommended = models.BooleanField(default=True, verbose_name='Рекомендуемый цвет')
    binding = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Цвет изделия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета изделия'
