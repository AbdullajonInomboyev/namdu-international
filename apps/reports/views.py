from django.shortcuts import render
from .models import AnnualReport


def index(request):
    reports = AnnualReport.objects.filter(is_public=True).order_by('-year')
    type_filter = request.GET.get('type')
    if type_filter:
        reports = reports.filter(report_type=type_filter)
    return render(request, 'reports/index.html', {
        'reports': reports,
        'types': AnnualReport.TYPE_CHOICES,
        'selected_type': type_filter,
    })
