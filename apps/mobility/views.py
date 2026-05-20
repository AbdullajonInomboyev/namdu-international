from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import MobilityProgram, MobilityStudent


def index(request):
    programs = MobilityProgram.objects.filter(is_active=True).select_related('host_country', 'host_university')
    page = Paginator(programs, 9).get_page(request.GET.get('page'))
    stats = {
        'total_outgoing': MobilityStudent.objects.filter(direction='outgoing').count(),
        'total_incoming': MobilityStudent.objects.filter(direction='incoming').count(),
        'total_programs': MobilityProgram.objects.filter(is_active=True).count(),
    }
    return render(request, 'mobility/index.html', {'page_obj': page, 'stats': stats})
