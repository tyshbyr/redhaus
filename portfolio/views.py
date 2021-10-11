from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
location = 'portfolio'
def portfolio_page(request):
    project_list = Project.objects.filter(to_publish=True)
    return render(request, 'portfolio/portfolio_page.html', {'project_list':project_list, 'location':location})


def project_page(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    images = Gallery.objects.filter(binding=project.pk)
    return render(request, 'portfolio/project_page.html', {'project':project, 'images':images, 'location':location})
