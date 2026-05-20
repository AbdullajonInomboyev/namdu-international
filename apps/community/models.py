from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CommunityProject(models.Model):
    title_uz = models.CharField(_("Nomi (UZ)"), max_length=400)
    title_en = models.CharField(_("Nomi (EN)"), max_length=400, blank=True)
    description_uz = RichTextUploadingField(_("Tavsif (UZ)"), blank=True)
    description_en = RichTextUploadingField(_("Tavsif (EN)"), blank=True)
    image = models.ImageField(_("Rasm"), upload_to='community/', blank=True, null=True)
    start_date = models.DateField(_("Boshlanishi"), null=True, blank=True)
    end_date = models.DateField(_("Tugashi"), null=True, blank=True)
    beneficiaries = models.PositiveIntegerField(_("Foydalanuvchilar soni"), default=0)
    location_uz = models.CharField(_("Joylashuv"), max_length=300, blank=True)
    sdg_connection = models.CharField(_("SDG bog'lanishi"), max_length=100, blank=True)
    is_active = models.BooleanField(_("Faol"), default=True)
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Jamoaviy loyiha")
        verbose_name_plural = _("Jamoaviy loyihalar")
        ordering = ['-start_date']

    def __str__(self):
        return self.title_uz
