from django.db import models
from django.utils.translation import gettext_lazy as _


class ResearchArea(models.Model):
    name_uz = models.CharField(_("Soha (UZ)"), max_length=200)
    name_en = models.CharField(_("Soha (EN)"), max_length=200, blank=True)

    class Meta:
        verbose_name = _("Ilmiy soha")
        verbose_name_plural = _("Ilmiy sohalar")

    def __str__(self):
        return self.name_uz


class Publication(models.Model):
    QUARTILE_CHOICES = [('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4'), ('OA', 'Open Access')]
    DATABASE_CHOICES = [
        ('scopus', 'Scopus'), ('wos', 'Web of Science'),
        ('google_scholar', 'Google Scholar'), ('other', 'Boshqa'),
    ]
    title = models.CharField(_("Maqola nomi"), max_length=500)
    authors = models.CharField(_("Mualliflar"), max_length=500)
    journal = models.CharField(_("Jurnal"), max_length=300)
    year = models.PositiveIntegerField(_("Yil"))
    quartile = models.CharField(_("Kvartil"), max_length=5, choices=QUARTILE_CHOICES, blank=True)
    database = models.CharField(_("Baza"), max_length=30, choices=DATABASE_CHOICES, default='scopus')
    doi = models.CharField(_("DOI"), max_length=200, blank=True)
    url = models.URLField(_("URL"), blank=True)
    citations = models.PositiveIntegerField(_("Iqtiboslar soni"), default=0)
    research_area = models.ForeignKey(ResearchArea, on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name=_("Ilmiy soha"))
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Nashr")
        verbose_name_plural = _("Nashrlar")
        ordering = ['-year', '-citations']

    def __str__(self):
        return f"{self.title[:80]} ({self.year})"


class ResearchGrant(models.Model):
    STATUS_CHOICES = [
        ('active', _('Faol')), ('completed', _('Yakunlangan')), ('pending', _('Kutilmoqda')),
    ]
    title_uz = models.CharField(_("Grant nomi (UZ)"), max_length=400)
    title_en = models.CharField(_("Grant nomi (EN)"), max_length=400, blank=True)
    funder = models.CharField(_("Moliyalovchi tashkilot"), max_length=300)
    amount = models.DecimalField(_("Miqdor (USD)"), max_digits=12, decimal_places=2, null=True, blank=True)
    start_date = models.DateField(_("Boshlanish sanasi"))
    end_date = models.DateField(_("Tugash sanasi"), null=True, blank=True)
    status = models.CharField(_("Holati"), max_length=20, choices=STATUS_CHOICES, default='active')
    principal_investigator = models.CharField(_("Asosiy tadqiqotchi"), max_length=200)
    description_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Grant")
        verbose_name_plural = _("Grantlar")
        ordering = ['-start_date']

    def __str__(self):
        return self.title_uz
