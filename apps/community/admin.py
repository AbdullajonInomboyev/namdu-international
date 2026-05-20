from django.contrib import admin
from .models import CommunityProject


@admin.register(CommunityProject)
class CommunityProjectAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'start_date', 'beneficiaries', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_editable = ('is_active', 'is_featured')
    search_fields = ('title_uz', 'title_en')
