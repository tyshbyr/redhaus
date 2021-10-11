from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
path('', views.order_page, name='order_page'),
]
