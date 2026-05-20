from django.db import models
from django.utils.translation import gettext_lazy as _


class RankingAgency(models.Model):
    name = models.CharField(_("Agentlik nomi"), max_length=100)
    short_name = models.CharField(_("Qisqa nomi"), max_length=20)
    website = models.URLField(_("Veb-sayt"), blank=True)
    logo = models.ImageField(_("Logo"), upload_to='rankings/logos/', blank=True, null=True)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)

    class Meta:
        verbose_name = _("Reyting agentligi")
        verbose_name_plural = _("Reyting agentliklari")

    def __str__(self):
        return self.short_name


class Ranking(models.Model):
    agency = models.ForeignKey(RankingAgency, on_delete=models.CASCADE,
                                verbose_name=_("Agentlik"), related_name='rankings')
    ranking_name = models.CharField(_("Reyting nomi"), max_length=300)
    year = models.PositiveIntegerField(_("Yil"))
    position = models.CharField(_("O'rin"), max_length=100)
    score = models.FloatField(_("Ball"), null=True, blank=True)
    category = models.CharField(_("Kategoriya"), max_length=200, blank=True)
    certificate = models.FileField(_("Sertifikat"), upload_to='rankings/certs/', blank=True, null=True)
    details_url = models.URLField(_("Batafsil URL"), blank=True)
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Reyting")
        verbose_name_plural = _("Reytinglar")
        ordering = ['-year', 'agency']

    def __str__(self):
        return f"{self.agency.short_name} — {self.ranking_name} ({self.year}): {self.position}"
