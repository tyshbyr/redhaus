from django.urls import path
from . import views

app_name = 'designers'

urlpatterns = [
path('', views.designers_page, name='designers_page'),
]
