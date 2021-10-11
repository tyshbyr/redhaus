from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
path('', views.catalog_page, name='catalog_page'),
path('kit/<slug:kit_slug>/', views.kit_page, name='kit_page'),
path('product/<slug:product_slug>/', views.product_page, name='product_page'),
path('products/<slug:products_slug>/', views.products_page, name='products_page'),
path('kits/<slug:kits_slug>/', views.kits_page, name='kits_page'),
]
