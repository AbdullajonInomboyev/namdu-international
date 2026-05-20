from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Conference


def index(request):
    conferences = Conference.objects.filter(is_active=True).order_by('-start_date')
    page = Paginator(conferences, 9).get_page(request.GET.get('page'))
    return render(request, 'conferences/index.html', {'page_obj': page})

def detail(request, slug):
    conference = get_object_or_404(Conference, slug=slug, is_active=True)
    return render(request, 'conferences/detail.html', {'conference': conference})
