from django.contrib import admin
from .models import VisitingProfessor


@admin.register(VisitingProfessor)
class VisitingProfessorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'home_university', 'country', 'status', 'visit_start', 'is_featured')
    list_filter = ('status', 'country', 'is_featured')
    list_editable = ('is_featured',)
    search_fields = ('full_name', 'specialization_uz', 'specialization_en')
    fieldsets = (
        ("Asosiy", {'fields': ('full_name', 'title', 'home_university', 'country', 'photo')}),
        ("Mutaxassislik", {'fields': ('specialization_uz', 'specialization_en', 'bio_uz', 'bio_en')}),
        ("Tashrif", {'fields': ('visit_start', 'visit_end', 'lecture_topic_uz', 'status', 'is_featured')}),
    )
