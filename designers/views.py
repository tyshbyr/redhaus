from django.shortcuts import render

# Create your views here.
location = 'designers'


def designers_page(request):
    return render(request, 'designers/designers_page.html', {'location':location})
