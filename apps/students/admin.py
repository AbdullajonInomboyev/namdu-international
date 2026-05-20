from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import InternationalStudent, StudentCountryStat


@admin.register(InternationalStudent)
class InternationalStudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'country', 'degree', 'faculty', 'admission_year', 'status', 'is_featured')
    list_filter = ('degree', 'status', 'country', 'admission_year', 'is_featured')
    list_editable = ('is_featured',)
    search_fields = ('first_name', 'last_name', 'faculty')


@admin.register(StudentCountryStat)
class StudentCountryStatAdmin(admin.ModelAdmin):
    list_display = ('country', 'count', 'academic_year')
    list_editable = ('count',)
