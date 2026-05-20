from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.partnerships.models import Country, Partner


class MobilityProgram(models.Model):
    TYPE_CHOICES = [
        ('erasmus', 'Erasmus+'), ('daad', 'DAAD'), ('fulbright', 'Fulbright'),
        ('other', _('Boshqa')),
    ]
    name = models.CharField(_("Dastur nomi"), max_length=300)
    program_type = models.CharField(_("Tur"), max_length=30, choices=TYPE_CHOICES, default='other')
    host_university = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name=_("Qabul qiluvchi universitet"))
    host_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                      verbose_name=_("Davlat"))
    duration_months = models.PositiveIntegerField(_("Muddati (oy)"), default=6)
    funding = models.CharField(_("Moliyalashtirish"), max_length=200, blank=True)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    description_en = models.TextField(_("Tavsif (EN)"), blank=True)
    deadline = models.DateField(_("Ariza oxirgi muddati"), null=True, blank=True)
    is_active = models.BooleanField(_("Faol"), default=True)
    url = models.URLField(_("Batafsil URL"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Mobillik dasturi")
        verbose_name_plural = _("Mobillik dasturlari")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class MobilityStudent(models.Model):
    DIRECTION_CHOICES = [('outgoing', _('Chiquvchi')), ('incoming', _('Kiruvchi'))]
    full_name = models.CharField(_("To'liq ism"), max_length=200)
    program = models.ForeignKey(MobilityProgram, on_delete=models.SET_NULL, null=True,
                                 verbose_name=_("Dastur"), related_name='students')
    direction = models.CharField(_("Yo'nalish"), max_length=20, choices=DIRECTION_CHOICES)
    faculty = models.CharField(_("Fakultet"), max_length=200)
    academic_year = models.CharField(_("O'quv yili"), max_length=20)
    semester = models.PositiveIntegerField(_("Semestr"), choices=[(1, '1'), (2, '2')], default=1)
    home_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                      verbose_name=_("Vatani"), related_name='outgoing_students')

    class Meta:
        verbose_name = _("Mobillik talabasi")
        verbose_name_plural = _("Mobillik talabalari")
        ordering = ['-academic_year']

    def __str__(self):
        return f"{self.full_name} — {self.program}"
