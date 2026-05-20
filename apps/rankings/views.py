from django.shortcuts import render
from .models import Ranking, RankingAgency


def index(request):
    agencies = RankingAgency.objects.all()
    agency_filter = request.GET.get('agency')
    rankings = Ranking.objects.select_related('agency').order_by('-year')
    if agency_filter:
        rankings = rankings.filter(agency__pk=agency_filter)
    return render(request, 'rankings/index.html', {
        'rankings': rankings,
        'agencies': agencies,
        'selected_agency': agency_filter,
    })
