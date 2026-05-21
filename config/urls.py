from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "NamDU Xalqaro Bo'lim"
admin.site.site_title = "NamDU Admin"
admin.site.index_title = "Boshqaruv paneli"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.core.urls')),
    path('news/', include('apps.news.urls')),
    path('rankings/', include('apps.rankings.urls')),
    path('sustainability/', include('apps.sustainability.urls')),
    path('research/', include('apps.research.urls')),
    path('partnerships/', include('apps.partnerships.urls')),
    path('mobility/', include('apps.mobility.urls')),
    path('students/', include('apps.students.urls')),
    path('professors/', include('apps.professors.urls')),
    path('conferences/', include('apps.conferences.urls')),
    path('community/', include('apps.community.urls')),
    path('reports/', include('apps.reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)