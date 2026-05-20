from django.shortcuts import render
from django.core.paginator import Paginator
from .models import InternationalStudent, StudentCountryStat


def index(request):
    students = InternationalStudent.objects.select_related('country').order_by('-admission_year')
    degree_filter = request.GET.get('degree')
    if degree_filter:
        students = students.filter(degree=degree_filter)
    page = Paginator(students, 12).get_page(request.GET.get('page'))
    country_stats = StudentCountryStat.objects.select_related('country').order_by('-count')[:10]
    featured = InternationalStudent.objects.filter(is_featured=True).select_related('country')[:4]
    return render(request, 'students/index.html', {
        'page_obj': page,
        'country_stats': country_stats,
        'featured': featured,
        'selected_degree': degree_filter,
        'degrees': InternationalStudent.DEGREE_CHOICES,
        'total': InternationalStudent.objects.count(),
    })
