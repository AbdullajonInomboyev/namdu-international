from django.db import models
from django.utils.translation import gettext_lazy as _


class AnnualReport(models.Model):
    TYPE_CHOICES = [
        ('annual', _('Yillik hisobot')), ('sustainability', _('Barqarorlik')),
        ('research', _('Ilmiy faoliyat')), ('mobility', _('Akademik mobillik')),
        ('policy', _('Siyosat hujjati')), ('other', _('Boshqa')),
    ]
    title_uz = models.CharField(_("Nomi (UZ)"), max_length=400)
    title_ru = models.CharField(_("Nomi (RU)"), max_length=400, blank=True)
    title_en = models.CharField(_("Nomi (EN)"), max_length=400, blank=True)
    report_type = models.CharField(_("Tur"), max_length=30, choices=TYPE_CHOICES, default='annual')
    year = models.PositiveIntegerField(_("Yil"))
    cover_image = models.ImageField(_("Muqova"), upload_to='reports/covers/', blank=True, null=True)
    file_uz = models.FileField(_("Fayl (UZ)"), upload_to='reports/files/', blank=True, null=True)
    file_en = models.FileField(_("Fayl (EN)"), upload_to='reports/files/', blank=True, null=True)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    pages = models.PositiveIntegerField(_("Sahifalar soni"), null=True, blank=True)
    is_public = models.BooleanField(_("Ommaviy"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Hisobot")
        verbose_name_plural = _("Hisobotlar")
        ordering = ['-year', 'report_type']

    def __str__(self):
        return f"{self.title_uz} ({self.year})"
