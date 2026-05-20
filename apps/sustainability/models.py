from django.db import models
from django.utils.translation import gettext_lazy as _


class SDGGoal(models.Model):
    number = models.PositiveIntegerField(_("SDG raqami"), unique=True)
    name_uz = models.CharField(_("Nomi (UZ)"), max_length=300)
    name_en = models.CharField(_("Nomi (EN)"), max_length=300, blank=True)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    color = models.CharField(_("Rang"), max_length=20, default="#1ab69d")
    icon = models.ImageField(_("SDG ikonkasi"), upload_to='sdg/icons/', blank=True, null=True)
    namdu_activities_uz = models.TextField(_("NamDU faoliyati (UZ)"), blank=True)
    namdu_activities_en = models.TextField(_("NamDU faoliyati (EN)"), blank=True)
    is_active = models.BooleanField(_("Faol"), default=True)

    class Meta:
        verbose_name = _("SDG Maqsad")
        verbose_name_plural = _("SDG Maqsadlar")
        ordering = ['number']

    def __str__(self):
        return f"SDG {self.number}: {self.name_uz}"


class GreenMetric(models.Model):
    CATEGORY_CHOICES = [
        ('co2', _('CO₂ qisqarish')), ('trees', _('Daraxtlar')),
        ('recycling', _('Qayta ishlash')), ('energy', _('Energiya tejash')),
        ('water', _('Suv tejash')), ('other', _('Boshqa')),
    ]
    category = models.CharField(_("Kategoriya"), max_length=20, choices=CATEGORY_CHOICES)
    value = models.CharField(_("Qiymat"), max_length=50)
    unit = models.CharField(_("Birlik"), max_length=50, blank=True)
    description_uz = models.CharField(_("Tavsif (UZ)"), max_length=200, blank=True)
    year = models.PositiveIntegerField(_("Yil"), default=2024)
    icon_class = models.CharField(_("Ikonka"), max_length=100, blank=True)

    class Meta:
        verbose_name = _("Green ko'rsatkich")
        verbose_name_plural = _("Green ko'rsatkichlar")
        ordering = ['category']

    def __str__(self):
        return f"{self.get_category_display()}: {self.value}{self.unit}"
