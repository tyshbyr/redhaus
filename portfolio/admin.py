from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

class GalleryAdmin(admin.StackedInline):
    model = Gallery
    fields = ('image', 'get_image')
    readonly_fields = ('get_image',)
    extra = 0

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="130px"')
        else:
            return 'нет картинки'
    get_image.short_description = 'Фотография'


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'date', 'short_description', 'get_thumbnail', 'to_publish')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'slug', 'date', 'short_description', 'description', 'thumbnail', 'get_thumbnail', 'to_publish')
    readonly_fields = ('get_thumbnail', 'date')
    inlines = [GalleryAdmin,]

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" width="130px"')
        else:
            return 'нет картинки'
    get_thumbnail.short_description = 'Миниатюра'


admin.site.register(Project, ProjectAdmin)
