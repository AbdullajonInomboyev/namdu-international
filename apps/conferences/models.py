from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Conference(models.Model):
    FORMAT_CHOICES = [
        ('offline', _('Offline')), ('online', _('Online')), ('hybrid', _('Gibrid')),
    ]
    title_uz = models.CharField(_("Nomi (UZ)"), max_length=400)
    title_ru = models.CharField(_("Nomi (RU)"), max_length=400, blank=True)
    title_en = models.CharField(_("Nomi (EN)"), max_length=400, blank=True)
    slug = models.SlugField(max_length=450, unique=True, blank=True)
    description_uz = RichTextUploadingField(_("Tavsif (UZ)"), blank=True)
    description_en = RichTextUploadingField(_("Tavsif (EN)"), blank=True)
    cover_image = models.ImageField(_("Muqova rasmi"), upload_to='conferences/', blank=True, null=True)
    start_date = models.DateField(_("Boshlanish sanasi"))
    end_date = models.DateField(_("Tugash sanasi"), null=True, blank=True)
    location_uz = models.CharField(_("Manzil (UZ)"), max_length=300, blank=True)
    format = models.CharField(_("Format"), max_length=20, choices=FORMAT_CHOICES, default='offline')
    participants_count = models.PositiveIntegerField(_("Ishtirokchilar soni"), default=0)
    countries_count = models.PositiveIntegerField(_("Davlatlar soni"), default=0)
    registration_url = models.URLField(_("Ro'yxatdan o'tish URL"), blank=True)
    registration_deadline = models.DateField(_("Ariza muddati"), null=True, blank=True)
    is_active = models.BooleanField(_("Faol"), default=True)
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Konferensiya")
        verbose_name_plural = _("Konferensiyalar")
        ordering = ['-start_date']

    def __str__(self):
        return self.title_uz

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title_en or self.title_uz) or f"conf-{self.pk}"
        super().save(*args, **kwargs)
