from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('production/', views.production_page, name='production_page'),
]

