from django.contrib import admin
from .models import SDGGoal, GreenMetric


@admin.register(SDGGoal)
class SDGGoalAdmin(admin.ModelAdmin):
    list_display = ('number', 'name_uz', 'color', 'is_active')
    list_editable = ('is_active',)


@admin.register(GreenMetric)
class GreenMetricAdmin(admin.ModelAdmin):
    list_display = ('category', 'value', 'unit', 'year')
    list_editable = ('value',)
    list_filter = ('year', 'category')
