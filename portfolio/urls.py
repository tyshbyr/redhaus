from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
path('', views.portfolio_page, name='portfolio_page'),
path('<slug:project_slug>/', views.project_page, name='project_page'),
]
