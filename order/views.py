from django.shortcuts import render

# Create your views here.
location = 'catalog'

def order_page(request):
    return render(request, 'order/order_page.html', {'location':location})
