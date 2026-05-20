from django.shortcuts import render
from django.core.paginator import Paginator
from .models import CommunityProject


def index(request):
    projects = CommunityProject.objects.filter(is_active=True).order_by('-start_date')
    page = Paginator(projects, 9).get_page(request.GET.get('page'))
    return render(request, 'community/index.html', {'page_obj': page})
