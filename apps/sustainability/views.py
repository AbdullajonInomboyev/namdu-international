from django.shortcuts import render
from .models import SDGGoal, GreenMetric


def index(request):
    sdgs = SDGGoal.objects.filter(is_active=True).order_by('number')
    metrics = GreenMetric.objects.all()
    return render(request, 'sustainability/index.html', {'sdgs': sdgs, 'metrics': metrics})
