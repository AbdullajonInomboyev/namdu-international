from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, NewsCategory


def index(request):
    news = News.objects.filter(is_published=True).select_related('category').order_by('-published_at')
    cat = request.GET.get('category')
    if cat:
        news = news.filter(category__slug=cat)
    page = Paginator(news, 9).get_page(request.GET.get('page'))
    categories = NewsCategory.objects.all()
    return render(request, 'news/index.html', {
        'page_obj': page,
        'categories': categories,
        'selected_cat': cat,
    })

def detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    news.views += 1
    news.save(update_fields=['views'])
    related = News.objects.filter(is_published=True).exclude(pk=news.pk).order_by('-published_at')[:3]
    return render(request, 'news/detail.html', {'news': news, 'related': related})
