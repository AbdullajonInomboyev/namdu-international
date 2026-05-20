from django.contrib import admin
from .models import RankingAgency, Ranking


@admin.register(RankingAgency)
class RankingAgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'website')


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ('agency', 'ranking_name', 'year', 'position', 'score', 'is_featured')
    list_filter = ('agency', 'year', 'is_featured')
    list_editable = ('is_featured',)
    search_fields = ('ranking_name', 'category')
    date_hierarchy = None
