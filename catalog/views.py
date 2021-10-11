from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
location = 'catalog'


def check_object_class(category):
    if type(category) == ProductCategory:
        return True
    else:
        return False


def create_objects_page(request, cat, object, slug):
    try:
        collection = int(request.GET['collection'])
    except:
        collection = 'all'
    category = get_object_or_404(cat, slug=slug)
    is_product = check_object_class(category)
    objects_list = object.objects.filter(category=category.pk, to_publish=True)
    object_collection_list = [{'collection':obj.collection, 'collection_id':obj.collection_id} for obj in objects_list]
    object_collection_list_filter = [dict(t) for t in set([tuple(d.items()) for d in object_collection_list])]
    return render(request, 'catalog/objects_page.html', {'category':category,
                                                        'objects_list':objects_list,
                                                        'is_product':is_product,
                                                        'location':location,
                                                        'object_collection_list_filter':object_collection_list_filter,
                                                        'collection':collection})


def create_object_page(request, model, sliders_model, colors_model, cat_model, slug):
    object = get_object_or_404(model, slug=slug)
    slider_list = sliders_model.objects.filter(binding=object.pk)
    color_list = colors_model.objects.filter(binding=object.pk)
    try:
        other_objects_list = Product.objects.filter(kit=object.kit, to_publish=True)
        kit = get_object_or_404(Kit, pk=object.kit_id)
    except:
        other_objects_list = Product.objects.filter(kit=object.pk, to_publish=True)
        kit = None
    category = get_object_or_404(cat_model, pk=object.category_id)
    is_product = check_object_class(category)

    return render(request, 'catalog/object_page.html', {
                                                        'location':location,
                                                        'object':object,
                                                        'slider_list':slider_list,
                                                        'color_list':color_list,
                                                        'other_objects_list':other_objects_list,
                                                        'category':category,
                                                        'is_product':is_product,
                                                        'kit':kit
                                                        })



def catalog_page(request):
    kits_list = KitCategory.objects.filter(to_publish=True)
    products_list = ProductCategory.objects.filter(to_publish=True)
    return render(request, 'catalog/catalog_page.html', {'kits_list':kits_list,
                                                            'products_list':products_list,
                                                            'location':location})


def kits_page(request, kits_slug):
    return create_objects_page(request, KitCategory, Kit, kits_slug)


def products_page(request, products_slug):
    return create_objects_page(request, ProductCategory, Product, products_slug)


def product_page(request, product_slug):
    return create_object_page(request, Product, SliderProduct, ColorProduct, ProductCategory, product_slug)


def kit_page(request, kit_slug):
    return create_object_page(request, Kit, SliderKit, ColorKit, KitCategory, kit_slug)
