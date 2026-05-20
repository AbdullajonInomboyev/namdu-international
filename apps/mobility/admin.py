from django.contrib import admin
from .models import MobilityProgram, MobilityStudent


class MobilityStudentInline(admin.TabularInline):
    model = MobilityStudent
    extra = 1
    fields = ('full_name', 'direction', 'faculty', 'academic_year', 'home_country')


@admin.register(MobilityProgram)
class MobilityProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_type', 'host_country', 'duration_months', 'deadline', 'is_active')
    list_filter = ('program_type', 'host_country', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name',)
    inlines = [MobilityStudentInline]


@admin.register(MobilityStudent)
class MobilityStudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'program', 'direction', 'faculty', 'academic_year')
    list_filter = ('direction', 'academic_year', 'home_country')
    search_fields = ('full_name', 'faculty')
