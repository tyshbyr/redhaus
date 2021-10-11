from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.

class KitCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'price', 'short_description', 'get_thumbnail', 'to_publish')
    list_editable = ('price',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'slug', 'short_description', 'thumbnail', 'get_thumbnail', 'price', 'to_publish')
    readonly_fields = ('get_thumbnail',)

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" width="130px"')
        else:
            return 'нет картинки'
    get_thumbnail.short_description = 'Миниатюра'



class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'price', 'short_description', 'get_thumbnail', 'to_publish')
    list_editable = ('price',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'slug', 'short_description', 'thumbnail', 'get_thumbnail', 'price', 'to_publish')
    readonly_fields = ('get_thumbnail',)

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" width="130px"')
        else:
            return 'нет картинки'
    get_thumbnail.short_description = 'Миниатюра'




class SliderKitAdmin(admin.StackedInline):
    model = SliderKit
    fields = ('image', 'get_image')
    readonly_fields = ('get_image',)
    extra = 0

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="130px"')
        else:
            return 'нет картинки'
    get_image.short_description = 'Миниатюра'


class ColorKitAdmin(admin.StackedInline):
    model = ColorKit
    fields = ('title', 'image', 'render', 'recommended', 'get_image', 'get_render')
    readonly_fields = ('get_image','get_render')
    extra = 0

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="130px"')
        else:
            return 'нет картинки'
    get_image.short_description = 'Цвет'

    def get_render(self, obj):
        if obj.render:
            return mark_safe(f'<img src="{obj.render.url}" width="130px"')
        else:
            return 'нет картинки'
    get_render.short_description = 'Рендер'


class KitAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'price', 'collection', 'category', 'get_thumbnail', 'to_publish')
    list_filter = ('collection', 'category')
    list_editable = ('price',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'slug', 'short_description', 'description', 'info', 'thumbnail',
                        'get_thumbnail', 'price', 'collection', 'category', 'to_publish')
    readonly_fields = ('get_thumbnail',)
    inlines = [SliderKitAdmin, ColorKitAdmin]

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" width="130px"')
        else:
            return 'нет картинки'
    get_thumbnail.short_description = 'Миниатюра'




class SliderProductAdmin(admin.StackedInline):
    model = SliderProduct
    fields = ('image', 'get_image')
    readonly_fields = ('get_image',)
    extra = 0

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="130px"')
        else:
            return 'нет картинки'
    get_image.short_description = 'Миниатюра'


class ColorProductAdmin(admin.StackedInline):
    model = ColorProduct
    fields = ('title', 'image', 'render', 'recommended', 'get_image', 'get_render')
    readonly_fields = ('get_image','get_render')
    extra = 0

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="130px"')
        else:
            return 'нет картинки'
    get_image.short_description = 'Цвет'

    def get_render(self, obj):
        if obj.render:
            return mark_safe(f'<img src="{obj.render.url}" width="130px"')
        else:
            return 'нет картинки'
    get_render.short_description = 'Рендер'


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'price', 'collection', 'category', 'get_thumbnail', 'to_publish')
    list_filter = ('collection', 'category', 'kit')
    list_editable = ('price',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'slug', 'short_description', 'description', 'info', 'thumbnail',
                        'get_thumbnail', 'price', 'collection', 'category', 'kit', 'to_publish')
    readonly_fields = ('get_thumbnail',)
    inlines = [SliderProductAdmin, ColorProductAdmin]

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" width="130px"')
        else:
            return 'нет картинки'
    get_thumbnail.short_description = 'Миниатюра'





admin.site.register(Collection)
admin.site.register(KitCategory, KitCategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Kit, KitAdmin)
admin.site.register(Product, ProductAdmin)
#admin.site.register(SliderKit)
#admin.site.register(ColorKit)
#admin.site.register(SliderProduct)
#admin.site.register(ColorProduct)
