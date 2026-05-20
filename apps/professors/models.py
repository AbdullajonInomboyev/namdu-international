from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.partnerships.models import Country, Partner


class VisitingProfessor(models.Model):
    STATUS_CHOICES = [
        ('current', _('Hozirgi')), ('past', _('O\'tgan')), ('upcoming', _('Kelasi')),
    ]
    full_name = models.CharField(_("To'liq ism"), max_length=200)
    title = models.CharField(_("Unvon"), max_length=200, blank=True)
    home_university = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name=_("Asosiy universitet"))
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                 verbose_name=_("Davlat"))
    photo = models.ImageField(_("Rasm"), upload_to='professors/photos/', blank=True, null=True)
    specialization_uz = models.CharField(_("Mutaxassisligi (UZ)"), max_length=300, blank=True)
    specialization_en = models.CharField(_("Mutaxassisligi (EN)"), max_length=300, blank=True)
    bio_uz = models.TextField(_("Tarjimai hol (UZ)"), blank=True)
    bio_en = models.TextField(_("Tarjimai hol (EN)"), blank=True)
    visit_start = models.DateField(_("Tashrif boshlanishi"), null=True, blank=True)
    visit_end = models.DateField(_("Tashrif tugashi"), null=True, blank=True)
    lecture_topic_uz = models.CharField(_("Ma'ruza mavzusi (UZ)"), max_length=400, blank=True)
    status = models.CharField(_("Holati"), max_length=20, choices=STATUS_CHOICES, default='current')
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)

    class Meta:
        verbose_name = _("Mehmon professor")
        verbose_name_plural = _("Mehmon professorlar")
        ordering = ['-visit_start']

    def __str__(self):
        return f"{self.full_name} ({self.home_university})"
