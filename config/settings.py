# from pathlib import Path
# from decouple import config

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me-in-production')
# DEBUG = config('DEBUG', default=True, cast=bool)
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# INSTALLED_APPS = [
#     # Jazzmin - chiroyli admin panel (FIRST)
#     'jazzmin',

#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     # Third party
#     'ckeditor',
#     'ckeditor_uploader',
#     'rosetta',

#     # Local apps
#     'apps.core',
#     'apps.news',
#     'apps.rankings',
#     'apps.sustainability',
#     'apps.research',
#     'apps.partnerships',
#     'apps.mobility',
#     'apps.students',
#     'apps.professors',
#     'apps.conferences',
#     'apps.community',
#     'apps.reports',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'config.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'django.template.context_processors.i18n',
#                 'apps.core.context_processors.site_settings',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME', default='namdu_international'),
#         'USER': config('DB_USER', default='postgres'),
#         'PASSWORD': config('DB_PASSWORD', default=''),
#         'HOST': config('DB_HOST', default='localhost'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # Internationalization
# LANGUAGE_CODE = 'uz'
# TIME_ZONE = 'Asia/Tashkent'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# from django.utils.translation import gettext_lazy as _
# LANGUAGES = [
#     ('uz', _('O\'zbekcha')),
#     ('ru', _('Ruscha')),
#     ('en', _('Inglizcha')),
# ]
# LOCALE_PATHS = [BASE_DIR / 'locale']

# # Static & Media
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # CKEditor
# CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline', 'Strike'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
#             ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
#             ['Link', 'Unlink'],
#             ['Image', 'Table', 'HorizontalRule'],
#             ['Format', 'FontSize'],
#             ['TextColor', 'BGColor'],
#             ['Source'],
#         ],
#         'height': 400,
#         'width': '100%',
#         'extraPlugins': 'justify,colorbutton,format',
#     },
#     'minimal': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['Link', 'Unlink'],
#             ['Source'],
#         ],
#         'height': 200,
#         'width': '100%',
#     },
# }

# # Jazzmin Admin sozlamalari
# JAZZMIN_SETTINGS = {
#     "site_title": "NamDU Xalqaro",
#     "site_header": "NamDU Xalqaro Bo'lim",
#     "site_brand": "NamDU International",
#     "site_logo": None,
#     "login_logo": None,
#     "welcome_sign": "NamDU Xalqaro Bo'lim Admin Paneliga xush kelibsiz",
#     "copyright": "Namangan Davlat Universiteti",
#     "search_model": ["news.News", "partnerships.Partner", "students.InternationalStudent"],
#     "user_avatar": None,
#     "topmenu_links": [
#         {"name": "Saytga o'tish", "url": "/", "new_window": True, "icon": "fas fa-external-link-alt"},
#         {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
#     ],
#     "usermenu_links": [
#         {"name": "Saytga o'tish", "url": "/", "new_window": True},
#     ],
#     "show_sidebar": True,
#     "navigation_expanded": True,
#     "hide_apps": [],
#     "hide_models": [],
#     "order_with_respect_to": [
#         "core", "news", "partnerships", "students",
#         "mobility", "research", "rankings", "sustainability",
#         "professors", "conferences", "community", "reports",
#     ],
#     "icons": {
#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",
#         "auth.Group": "fas fa-users",
#         "core.SiteSettings": "fas fa-cog",
#         "core.StatCounter": "fas fa-chart-bar",
#         "core.HeroSlide": "fas fa-images",
#         "news.News": "fas fa-newspaper",
#         "news.NewsCategory": "fas fa-tags",
#         "rankings.Ranking": "fas fa-trophy",
#         "rankings.RankingAgency": "fas fa-star",
#         "sustainability.SDGGoal": "fas fa-leaf",
#         "sustainability.GreenMetric": "fas fa-seedling",
#         "research.Publication": "fas fa-book",
#         "research.ResearchGrant": "fas fa-flask",
#         "partnerships.Partner": "fas fa-handshake",
#         "partnerships.MOU": "fas fa-file-contract",
#         "mobility.MobilityProgram": "fas fa-plane",
#         "mobility.MobilityStudent": "fas fa-user-graduate",
#         "students.InternationalStudent": "fas fa-globe",
#         "students.StudentCountry": "fas fa-flag",
#         "professors.VisitingProfessor": "fas fa-chalkboard-teacher",
#         "conferences.Conference": "fas fa-microphone",
#         "community.CommunityProject": "fas fa-hands-helping",
#         "reports.AnnualReport": "fas fa-file-pdf",
#     },
#     "default_icon_parents": "fas fa-chevron-circle-right",
#     "default_icon_children": "fas fa-circle",
#     "related_modal_active": True,
#     "custom_css": "css/admin_custom.css",
#     "custom_js": None,
#     "use_google_fonts_cdn": True,
#     "show_ui_builder": False,
#     "changeform_format": "horizontal_tabs",
#     "changeform_format_overrides": {
#         "auth.user": "collapsible",
#         "auth.group": "vertical_tabs",
#     },
#     "language_chooser": True,
# }

# JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text": False,
#     "footer_small_text": False,
#     "body_small_text": False,
#     "brand_small_text": False,
#     "brand_colour": "navbar-success",
#     "accent": "accent-teal",
#     "navbar": "navbar-dark",
#     "no_navbar_border": False,
#     "navbar_fixed": True,
#     "layout_boxed": False,
#     "footer_fixed": False,
#     "sidebar_fixed": True,
#     "sidebar": "sidebar-dark-teal",
#     "sidebar_nav_small_text": False,
#     "sidebar_disable_expand": False,
#     "sidebar_nav_child_indent": True,
#     "sidebar_nav_compact_style": False,
#     "sidebar_nav_legacy_style": False,
#     "sidebar_nav_flat_style": False,
#     "theme": "default",
#     "dark_mode_theme": None,
#     "button_classes": {
#         "primary": "btn-outline-primary",
#         "secondary": "btn-outline-secondary",
#         "info": "btn-info",
#         "warning": "btn-warning",
#         "danger": "btn-danger",
#         "success": "btn-success",
#     },
# }
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me-in-production')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    # Jazzmin - chiroyli admin panel (FIRST)
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'ckeditor',
    'ckeditor_uploader',
    'rosetta',

    # Local apps
    'apps.core',
    'apps.news',
    'apps.rankings',
    'apps.sustainability',
    'apps.research',
    'apps.partnerships',
    'apps.mobility',
    'apps.students',
    'apps.professors',
    'apps.conferences',
    'apps.community',
    'apps.reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'apps.core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('uz', _('O\'zbekcha')),
    ('ru', _('Ruscha')),
    ('en', _('Inglizcha')),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

# Static & Media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['Link', 'Unlink'],
            ['Image', 'Table', 'HorizontalRule'],
            ['Format', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Source'],
        ],
        'height': 400,
        'width': '100%',
        'extraPlugins': 'justify,colorbutton,format',
    },
    'minimal': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Link', 'Unlink'],
            ['Source'],
        ],
        'height': 200,
        'width': '100%',
    },
}

# Jazzmin Admin sozlamalari
JAZZMIN_SETTINGS = {
    "site_title": "NamDU Xalqaro",
    "site_header": "NamDU Xalqaro Bo'lim",
    "site_brand": "NamDU International",
    "site_logo": None,
    "login_logo": None,
    "welcome_sign": "NamDU Xalqaro Bo'lim Admin Paneliga xush kelibsiz",
    "copyright": "Namangan Davlat Universiteti",
    "search_model": ["news.News", "partnerships.Partner", "students.InternationalStudent"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Saytga o'tish", "url": "/", "new_window": True, "icon": "fas fa-external-link-alt"},
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    "usermenu_links": [
        {"name": "Saytga o'tish", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "core", "news", "partnerships", "students",
        "mobility", "research", "rankings", "sustainability",
        "professors", "conferences", "community", "reports",
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core.SiteSettings": "fas fa-cog",
        "core.StatCounter": "fas fa-chart-bar",
        "core.HeroSlide": "fas fa-images",
        "news.News": "fas fa-newspaper",
        "news.NewsCategory": "fas fa-tags",
        "rankings.Ranking": "fas fa-trophy",
        "rankings.RankingAgency": "fas fa-star",
        "sustainability.SDGGoal": "fas fa-leaf",
        "sustainability.GreenMetric": "fas fa-seedling",
        "research.Publication": "fas fa-book",
        "research.ResearchGrant": "fas fa-flask",
        "partnerships.Partner": "fas fa-handshake",
        "partnerships.MOU": "fas fa-file-contract",
        "mobility.MobilityProgram": "fas fa-plane",
        "mobility.MobilityStudent": "fas fa-user-graduate",
        "students.InternationalStudent": "fas fa-globe",
        "students.StudentCountry": "fas fa-flag",
        "professors.VisitingProfessor": "fas fa-chalkboard-teacher",
        "conferences.Conference": "fas fa-microphone",
        "community.CommunityProject": "fas fa-hands-helping",
        "reports.AnnualReport": "fas fa-file-pdf",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": "css/admin_custom.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-teal",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}