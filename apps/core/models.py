from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteSettings(models.Model):
    office_name_uz = models.CharField(_("Bo'lim nomi (UZ)"), max_length=200, default="Xalqaro Aloqalar Bo'limi")
    office_name_ru = models.CharField(_("Bo'lim nomi (RU)"), max_length=200, default="Международный отдел")
    office_name_en = models.CharField(_("Bo'lim nomi (EN)"), max_length=200, default="International Office")
    slogan_uz = models.CharField(_("Slogan (UZ)"), max_length=300, default="Global Aloqalar, Mahalliy Muvaffaqiyat")
    slogan_ru = models.CharField(_("Slogan (RU)"), max_length=300, blank=True)
    slogan_en = models.CharField(_("Slogan (EN)"), max_length=300, blank=True)
    email = models.EmailField(_("Email"), default="international@namdu.uz")
    phone = models.CharField(_("Telefon"), max_length=50, default="+998 69 210-01-35")
    address_uz = models.CharField(_("Manzil (UZ)"), max_length=300, default="Namangan sh., Boburshox ko'chasi, 161-uy")
    address_ru = models.CharField(_("Manzil (RU)"), max_length=300, blank=True)
    address_en = models.CharField(_("Manzil (EN)"), max_length=300, blank=True)
    telegram = models.URLField(_("Telegram"), blank=True)
    facebook = models.URLField(_("Facebook"), blank=True)
    instagram = models.URLField(_("Instagram"), blank=True)
    youtube = models.URLField(_("YouTube"), blank=True)
    namdu_main_url = models.URLField(_("NamDU asosiy sayt"), default="https://namdu.uz")
    meta_keywords = models.TextField(_("Meta kalit so'zlar"), blank=True)
    meta_description_uz = models.TextField(_("Meta tavsif (UZ)"), blank=True)

    class Meta:
        verbose_name = _("Sayt sozlamalari")
        verbose_name_plural = _("Sayt sozlamalari")

    def __str__(self):
        return "Sayt sozlamalari"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class StatCounter(models.Model):
    partner_universities = models.PositiveIntegerField(_("Hamkor universitetlar"), default=47)
    partner_countries = models.PositiveIntegerField(_("Hamkor davlatlar"), default=28)
    exchange_students = models.PositiveIntegerField(_("Almashinuv talabalari"), default=312)
    scopus_articles = models.PositiveIntegerField(_("Scopus maqolalar"), default=189)
    active_grants = models.PositiveIntegerField(_("Aktiv grantlar"), default=32)
    visiting_professors = models.PositiveIntegerField(_("Mehmon professorlar"), default=24)
    mou_agreements = models.PositiveIntegerField(_("MOU shartnomalari"), default=63)
    conferences_held = models.PositiveIntegerField(_("O'tkazilgan konferensiyalar"), default=18)

    class Meta:
        verbose_name = _("Statistika raqamlar")
        verbose_name_plural = _("Statistika raqamlar")

    def __str__(self):
        return "Statistika"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_stats(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HeroSlide(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', _('Rasm')),
        ('gif', _('GIF animatsiya')),
        ('video', _('Video (MP4)')),
    ]
    title_uz = models.CharField(_("Sarlavha (UZ)"), max_length=200)
    title_ru = models.CharField(_("Sarlavha (RU)"), max_length=200, blank=True)
    title_en = models.CharField(_("Sarlavha (EN)"), max_length=200, blank=True)
    subtitle_uz = models.TextField(_("Tavsif (UZ)"), blank=True)
    subtitle_ru = models.TextField(_("Tavsif (RU)"), blank=True)
    subtitle_en = models.TextField(_("Tavsif (EN)"), blank=True)

    media_type = models.CharField(_("Media turi"), max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    image = models.ImageField(_("Rasm / GIF"), upload_to='hero/', blank=True, null=True,
                               help_text=_("Rasm yoki GIF fayl yuklang (.jpg, .png, .gif)"))
    video = models.FileField(_("Video (MP4)"), upload_to='hero/videos/', blank=True, null=True,
                              help_text=_("MP4 formatdagi video yuklang (max 50MB)"))
    video_poster = models.ImageField(_("Video muqova rasmi"), upload_to='hero/posters/', blank=True, null=True,
                                      help_text=_("Video yuklanayotganda ko'rsatiladigan rasm"))

    overlay_opacity = models.FloatField(_("Qoplaма qoralik (0-1)"), default=0.5,
                                         help_text=_("0 = shaffof, 1 = to'liq qora"))
    overlay_color = models.CharField(_("Qoplama rangi"), max_length=20, default="#000000")

    btn_text_uz = models.CharField(_("Tugma 1 matni (UZ)"), max_length=100, default="Batafsil")
    btn_url = models.CharField(_("Tugma 1 URL"), max_length=200, default="#")
    btn2_text_uz = models.CharField(_("Tugma 2 matni (UZ)"), max_length=100, blank=True)
    btn2_url = models.CharField(_("Tugma 2 URL"), max_length=200, blank=True)

    order = models.PositiveIntegerField(_("Tartib raqami"), default=0,
                                         help_text=_("0 = birinchi ko'rsatiladi"))
    is_active = models.BooleanField(_("Faol"), default=True)
    auto_play_duration = models.PositiveIntegerField(_("Ko'rsatish vaqti (soniya)"), default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Hero slayd")
        verbose_name_plural = _("Hero slaydlar")
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.order}. {self.title_uz} [{self.get_media_type_display()}]"


class QuickLink(models.Model):
    title_uz = models.CharField(_("Nomi (UZ)"), max_length=100)
    title_ru = models.CharField(_("Nomi (RU)"), max_length=100, blank=True)
    title_en = models.CharField(_("Nomi (EN)"), max_length=100, blank=True)
    description_uz = models.CharField(_("Tavsif (UZ)"), max_length=200, blank=True)
    icon_class = models.CharField(_("Icon class (remixicon)"), max_length=100, default="ri-global-line")
    url = models.URLField(_("URL"))
    color = models.CharField(_("Rang (hex)"), max_length=20, default="#1ab69d")
    order = models.PositiveIntegerField(_("Tartib"), default=0)
    is_active = models.BooleanField(_("Faol"), default=True)

    class Meta:
        verbose_name = _("Tez havola")
        verbose_name_plural = _("Tez havolalar")
        ordering = ['order']

    def __str__(self):
        return self.title_uz
