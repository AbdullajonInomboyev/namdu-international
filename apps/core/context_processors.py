from .models import SiteSettings, StatCounter, QuickLink


def site_settings(request):
    return {
        'site_settings': SiteSettings.get_settings(),
        'stats': StatCounter.get_stats(),
        'quick_links': QuickLink.objects.filter(is_active=True),
    }
