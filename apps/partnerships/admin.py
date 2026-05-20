from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Country, Partner, MOU


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'code')
    search_fields = ('name_uz', 'name_en', 'code')


class MOUInline(admin.TabularInline):
    model = MOU
    extra = 1
    fields = ('title_uz', 'signed_date', 'expiry_date', 'status', 'document')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'partner_type', 'partnership_since', 'is_active', 'is_featured', 'order')
    list_filter = ('partner_type', 'country', 'is_active', 'is_featured')
    list_editable = ('is_active', 'is_featured', 'order')
    search_fields = ('name', 'short_name')
    inlines = [MOUInline]
    fieldsets = (
        (_("Asosiy ma'lumot"), {
            'fields': ('name', 'short_name', 'country', 'partner_type', 'logo', 'website', 'partnership_since'),
        }),
        (_("Tavsif"), {
            'fields': ('description_uz', 'description_ru', 'description_en'),
            'classes': ('collapse',),
        }),
        (_("Sozlamalar"), {
            'fields': ('order', 'is_active', 'is_featured'),
        }),
    )


@admin.register(MOU)
class MOUAdmin(admin.ModelAdmin):
    list_display = ('partner', 'title_uz', 'signed_date', 'expiry_date', 'status')
    list_filter = ('status', 'signed_date')
    search_fields = ('title_uz', 'partner__name')
    date_hierarchy = 'signed_date'
