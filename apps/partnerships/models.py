from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name_uz = models.CharField(_("Davlat nomi (UZ)"), max_length=100)
    name_ru = models.CharField(_("Davlat nomi (RU)"), max_length=100, blank=True)
    name_en = models.CharField(_("Davlat nomi (EN)"), max_length=100, blank=True)
    code = models.CharField(_("Kod (ISO 3166-1 alpha-2)"), max_length=2)
    flag = models.ImageField(_("Bayroq"), upload_to='flags/', blank=True, null=True)

    class Meta:
        verbose_name = _("Davlat")
        verbose_name_plural = _("Davlatlar")
        ordering = ['name_uz']

    def __str__(self):
        return self.name_uz


class Partner(models.Model):
    TYPE_CHOICES = [
        ('university', _('Universitet')),
        ('research', _('Ilmiy markaz')),
        ('government', _('Davlat tashkiloti')),
        ('ngo', _('NNT')),
        ('other', _('Boshqa')),
    ]
    name = models.CharField(_("Nomi"), max_length=300)
    short_name = models.CharField(_("Qisqa nomi"), max_length=100, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                 verbose_name=_("Davlat"), related_name='partners')
    partner_type = models.CharField(_("Tur"), max_length=20, choices=TYPE_CHOICES, default='university')
    logo = models.ImageField(_("Logo"), upload_to='partners/logos/', blank=True, null=True)
    website = models.URLField(_("Veb-sayt"), blank=True)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    description_ru = models.TextField(_("Tavsif (RU)"), blank=True)
    description_en = models.TextField(_("Tavsif (EN)"), blank=True)
    partnership_since = models.PositiveIntegerField(_("Hamkorlik boshlanishi (yil)"), null=True, blank=True)
    order = models.PositiveIntegerField(_("Tartib"), default=0)
    is_active = models.BooleanField(_("Faol"), default=True)
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)

    class Meta:
        verbose_name = _("Hamkor")
        verbose_name_plural = _("Hamkorlar")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class MOU(models.Model):
    """Memorandum of Understanding — shartnomalar"""
    STATUS_CHOICES = [
        ('active', _('Faol')),
        ('expired', _('Muddati o\'tgan')),
        ('pending', _('Kutilmoqda')),
    ]
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE,
                                 verbose_name=_("Hamkor"), related_name='mous')
    title_uz = models.CharField(_("Shartnoma nomi (UZ)"), max_length=400)
    title_ru = models.CharField(_("Shartnoma nomi (RU)"), max_length=400, blank=True)
    title_en = models.CharField(_("Shartnoma nomi (EN)"), max_length=400, blank=True)
    signed_date = models.DateField(_("Imzolangan sana"))
    expiry_date = models.DateField(_("Muddati"), null=True, blank=True)
    status = models.CharField(_("Holati"), max_length=20, choices=STATUS_CHOICES, default='active')
    document = models.FileField(_("Hujjat (PDF)"), upload_to='mou/docs/', blank=True, null=True)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("MOU shartnoma")
        verbose_name_plural = _("MOU shartnomalar")
        ordering = ['-signed_date']

    def __str__(self):
        return f"{self.partner.name} — {self.title_uz[:60]}"
