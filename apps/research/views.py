from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Publication, ResearchGrant, ResearchArea


def index(request):
    pubs = Publication.objects.select_related('research_area').order_by('-year', '-citations')
    q_filter = request.GET.get('quartile')
    db_filter = request.GET.get('database')
    if q_filter:
        pubs = pubs.filter(quartile=q_filter)
    if db_filter:
        pubs = pubs.filter(database=db_filter)
    page = Paginator(pubs, 10).get_page(request.GET.get('page'))
    grants = ResearchGrant.objects.filter(status='active').order_by('-start_date')[:5]
    areas = ResearchArea.objects.all()
    return render(request, 'research/index.html', {
        'page_obj': page,
        'grants': grants,
        'areas': areas,
        'total_pubs': Publication.objects.count(),
        'total_citations': sum(Publication.objects.values_list('citations', flat=True)),
        'selected_quartile': q_filter,
        'selected_db': db_filter,
        'quartile_list': ['Q1', 'Q2', 'Q3', 'Q4', 'OA'],
    })