from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class NewsCategory(models.Model):
    name_uz = models.CharField(_("Nomi (UZ)"), max_length=100)
    name_ru = models.CharField(_("Nomi (RU)"), max_length=100, blank=True)
    name_en = models.CharField(_("Nomi (EN)"), max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    color = models.CharField(_("Rang"), max_length=20, default="#1ab69d")

    class Meta:
        verbose_name = _("Yangilik kategoriyasi")
        verbose_name_plural = _("Yangilik kategoriyalari")

    def __str__(self):
        return self.name_uz


class News(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name=_("Kategoriya"), related_name='news')
    title_uz = models.CharField(_("Sarlavha (UZ)"), max_length=300)
    title_ru = models.CharField(_("Sarlavha (RU)"), max_length=300, blank=True)
    title_en = models.CharField(_("Sarlavha (EN)"), max_length=300, blank=True)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    short_description_uz = models.TextField(_("Qisqa tavsif (UZ)"), blank=True)
    short_description_ru = models.TextField(_("Qisqa tavsif (RU)"), blank=True)
    short_description_en = models.TextField(_("Qisqa tavsif (EN)"), blank=True)
    body_uz = RichTextUploadingField(_("Matn (UZ)"), blank=True)
    body_ru = RichTextUploadingField(_("Matn (RU)"), blank=True)
    body_en = RichTextUploadingField(_("Matn (EN)"), blank=True)
    image = models.ImageField(_("Rasm"), upload_to='news/%Y/%m/')
    published_at = models.DateField(_("Nashr sanasi"), null=True, blank=True)
    is_published = models.BooleanField(_("Nashr qilingan"), default=True)
    is_featured = models.BooleanField(_("Asosiy sahifada"), default=False)
    views = models.PositiveIntegerField(_("Ko'rishlar"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Yangilik")
        verbose_name_plural = _("Yangiliklar")
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title_uz

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title_uz) or slugify(self.title_en) or f"news-{self.pk}"
            self.slug = base
        super().save(*args, **kwargs)

    def get_title(self, lang='uz'):
        return getattr(self, f'title_{lang}') or self.title_uz

    def get_body(self, lang='uz'):
        return getattr(self, f'body_{lang}') or self.body_uz
