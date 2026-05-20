from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.partnerships.models import Country


class InternationalStudent(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', _("Bakalavr")), ('master', _("Magistr")),
        ('phd', _("PhD")), ('exchange', _("Almashinuv")),
    ]
    STATUS_CHOICES = [
        ('studying', _("O'qimoqda")), ('graduated', _("Bitirgan")), ('exchange_out', _("Xorijda")),
    ]
    first_name = models.CharField(_("Ism"), max_length=100)
    last_name = models.CharField(_("Familiya"), max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                 verbose_name=_("Davlat"), related_name='students')
    degree = models.CharField(_("Daraja"), max_length=20, choices=DEGREE_CHOICES)
    faculty = models.CharField(_("Fakultet"), max_length=200)
    admission_year = models.PositiveIntegerField(_("Qabul yili"))
    status = models.CharField(_("Holati"), max_length=20, choices=STATUS_CHOICES, default='studying')
    photo = models.ImageField(_("Rasm"), upload_to='students/photos/', blank=True, null=True)
    testimonial_uz = models.TextField(_("Fikr (UZ)"), blank=True)
    testimonial_en = models.TextField(_("Fikr (EN)"), blank=True)
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Xalqaro talaba")
        verbose_name_plural = _("Xalqaro talabalar")
        ordering = ['-admission_year', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.country})"


class StudentCountryStat(models.Model):
    """Davlatlar bo'yicha talabalar statistikasi"""
    country = models.OneToOneField(Country, on_delete=models.CASCADE,
                                    verbose_name=_("Davlat"), related_name='student_stat')
    count = models.PositiveIntegerField(_("Talabalar soni"), default=0)
    academic_year = models.CharField(_("O'quv yili"), max_length=20, default="2024-2025")

    class Meta:
        verbose_name = _("Davlat bo'yicha talabalar")
        verbose_name_plural = _("Davlatlar bo'yicha talabalar")

    def __str__(self):
        return f"{self.country} — {self.count} ta"
