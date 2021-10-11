from django.shortcuts import render
from catalog.models import Kit

# Create your views here.
location = 'home'


def home_page(request):
    kit_list = Kit.objects.all()[0:3]
    return render(request, 'home/home_page.html', {'location':location,
                                                    'kit_list':kit_list})


def production_page(request):
    return render(request, 'home/production_page.html', {'location':location})
    
