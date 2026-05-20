from django.contrib import admin
from .models import AnnualReport


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'report_type', 'year', 'pages', 'is_public')
    list_filter = ('report_type', 'year', 'is_public')
    list_editable = ('is_public',)
    search_fields = ('title_uz', 'title_en')
