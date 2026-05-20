from django.contrib import admin
from .models import Conference


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'start_date', 'end_date', 'format', 'participants_count', 'is_active', 'is_featured')
    list_filter = ('format', 'is_active', 'is_featured', 'start_date')
    list_editable = ('is_active', 'is_featured')
    search_fields = ('title_uz', 'title_en')
    prepopulated_fields = {'slug': ('title_en',)}
    date_hierarchy = 'start_date'
    fieldsets = (
        ("Sarlavha", {'fields': ('title_uz', 'title_ru', 'title_en', 'slug')}),
        ("Tavsif", {'fields': ('description_uz', 'description_en', 'cover_image')}),
        ("Sana va joylashuv", {'fields': ('start_date', 'end_date', 'location_uz', 'format')}),
        ("Statistika", {'fields': ('participants_count', 'countries_count')}),
        ("Ro'yxatdan o'tish", {'fields': ('registration_url', 'registration_deadline')}),
        ("Sozlamalar", {'fields': ('is_active', 'is_featured')}),
    )
