from django.shortcuts import render
from django.core.paginator import Paginator
from .models import VisitingProfessor


def index(request):
    professors = VisitingProfessor.objects.select_related('country', 'home_university').order_by('-visit_start')
    status_filter = request.GET.get('status')
    if status_filter:
        professors = professors.filter(status=status_filter)
    page = Paginator(professors, 9).get_page(request.GET.get('page'))
    return render(request, 'professors/index.html', {
        'page_obj': page,
        'selected_status': status_filter,
        'statuses': VisitingProfessor.STATUS_CHOICES,
    })
