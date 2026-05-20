from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import SiteSettings, StatCounter, HeroSlide, QuickLink


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Bo'lim nomi"), {'fields': ('office_name_uz', 'office_name_ru', 'office_name_en')}),
        (_("Slogan"), {'fields': ('slogan_uz', 'slogan_ru', 'slogan_en')}),
        (_("Aloqa"), {'fields': ('email', 'phone', 'address_uz', 'address_ru', 'address_en')}),
        (_("Ijtimoiy tarmoqlar"), {'fields': ('telegram', 'facebook', 'instagram', 'youtube')}),
        (_("Boshqa"), {'fields': ('namdu_main_url', 'meta_keywords', 'meta_description_uz')}),
    )
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(StatCounter)
class StatCounterAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Statistika raqamlar"), {
            'fields': (
                ('partner_universities', 'partner_countries'),
                ('exchange_students', 'scopus_articles'),
                ('active_grants', 'visiting_professors'),
                ('mou_agreements', 'conferences_held'),
            ),
        }),
    )
    def has_add_permission(self, request):
        return not StatCounter.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('order', 'title_uz', 'media_type', 'preview_thumb', 'auto_play_duration', 'is_active')
    list_editable = ('order', 'is_active', 'auto_play_duration')
    list_display_links = ('title_uz',)
    list_filter = ('media_type', 'is_active')

    def preview_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.image.url)
        elif obj.video_poster:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.video_poster.url)
        elif obj.video:
            return format_html('<span style="color:var(--color-primary);">🎬 Video</span>')
        return '—'
    preview_thumb.short_description = 'Ko\'rinish'

    fieldsets = (
        (_("Sarlavha va tavsif"), {
            'fields': ('title_uz', 'title_ru', 'title_en', 'subtitle_uz', 'subtitle_ru', 'subtitle_en'),
        }),
        (_("Media (Rasm / GIF / Video)"), {
            'fields': ('media_type', 'image', 'video', 'video_poster'),
            'description': '⚠️ Media turini tanlang, keyin mos faylni yuklang. GIF uchun ham "Rasm" turini tanlang.',
        }),
        (_("Qoplama effekti"), {
            'fields': ('overlay_color', 'overlay_opacity'),
            'classes': ('collapse',),
        }),
        (_("Tugmalar"), {
            'fields': ('btn_text_uz', 'btn_url', 'btn2_text_uz', 'btn2_url'),
        }),
        (_("Sozlamalar"), {
            'fields': ('order', 'is_active', 'auto_play_duration'),
        }),
    )


@admin.register(QuickLink)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'url', 'color', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('title_uz',)
