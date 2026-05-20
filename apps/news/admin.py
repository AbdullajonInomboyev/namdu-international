from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import News, NewsCategory


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'slug', 'color')
    prepopulated_fields = {'slug': ('name_uz',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'published_at', 'is_published', 'is_featured', 'views')
    list_filter = ('is_published', 'is_featured', 'category', 'published_at')
    list_editable = ('is_published', 'is_featured')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    prepopulated_fields = {'slug': ('title_uz',)}
    date_hierarchy = 'published_at'
    readonly_fields = ('views', 'created_at', 'updated_at')
    fieldsets = (
        (_("O'zbekcha"), {
            'fields': ('title_uz', 'short_description_uz', 'body_uz'),
        }),
        (_("Ruscha"), {
            'classes': ('collapse',),
            'fields': ('title_ru', 'short_description_ru', 'body_ru'),
        }),
        (_("Inglizcha"), {
            'classes': ('collapse',),
            'fields': ('title_en', 'short_description_en', 'body_en'),
        }),
        (_("Meta"), {
            'fields': ('slug', 'category', 'image', 'published_at', 'is_published', 'is_featured'),
        }),
        (_("Statistika"), {
            'fields': ('views', 'created_at', 'updated_at'),
        }),
    )
