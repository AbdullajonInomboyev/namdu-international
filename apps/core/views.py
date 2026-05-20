from django.shortcuts import render
from .models import HeroSlide, StatCounter
from apps.news.models import News
from apps.partnerships.models import Partner
from apps.conferences.models import Conference


def home(request):
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    latest_news = News.objects.filter(is_published=True).order_by('-published_at')[:3]
    partners = Partner.objects.filter(is_active=True).order_by('order')[:12]
    upcoming_conferences = Conference.objects.filter(is_active=True).order_by('start_date')[:3]
    return render(request, 'core/home.html', {
        'slides': slides,
        'latest_news': latest_news,
        'partners': partners,
        'upcoming_conferences': upcoming_conferences,
    })
