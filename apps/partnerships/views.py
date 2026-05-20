from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Partner, MOU, Country


def index(request):
    country_filter = request.GET.get('country')
    type_filter = request.GET.get('type')
    partners = Partner.objects.filter(is_active=True).select_related('country')
    if country_filter:
        partners = partners.filter(country__code=country_filter)
    if type_filter:
        partners = partners.filter(partner_type=type_filter)
    paginator = Paginator(partners, 12)
    page = paginator.get_page(request.GET.get('page'))
    countries = Country.objects.filter(partners__is_active=True).distinct()
    recent_mous = MOU.objects.filter(status='active').select_related('partner').order_by('-signed_date')[:5]
    return render(request, 'partnerships/index.html', {
        'page_obj': page,
        'countries': countries,
        'recent_mous': recent_mous,
        'total': Partner.objects.filter(is_active=True).count(),
        'selected_country': country_filter,
        'selected_type': type_filter,
        'partner_types': Partner.TYPE_CHOICES,
    })

def detail(request, pk):
    partner = get_object_or_404(Partner, pk=pk, is_active=True)
    mous = partner.mous.all().order_by('-signed_date')
    return render(request, 'partnerships/detail.html', {'partner': partner, 'mous': mous})

def mou_list(request):
    mous = MOU.objects.select_related('partner', 'partner__country').order_by('-signed_date')
    if request.GET.get('status'):
        mous = mous.filter(status=request.GET['status'])
    page = Paginator(mous, 15).get_page(request.GET.get('page'))
    return render(request, 'partnerships/mou_list.html', {'page_obj': page})
