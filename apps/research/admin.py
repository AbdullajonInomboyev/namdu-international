from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Publication, ResearchGrant, ResearchArea


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_en')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'journal', 'year', 'quartile', 'database', 'citations', 'is_featured')
    list_filter = ('quartile', 'database', 'year', 'research_area', 'is_featured')
    list_editable = ('is_featured',)
    search_fields = ('title', 'authors', 'journal')
    list_per_page = 30


@admin.register(ResearchGrant)
class ResearchGrantAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'funder', 'principal_investigator', 'amount', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'funder')
    search_fields = ('title_uz', 'title_en', 'funder', 'principal_investigator')
