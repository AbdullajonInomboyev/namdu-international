"""
python manage.py shell < load_data.py
"""
from django.utils import timezone
now = timezone.now()

# ===== CORE =====
from apps.core.models import SiteSettings, StatCounter, QuickLink, HeroSlide

SiteSettings.objects.update_or_create(pk=1, defaults={
    'office_name_uz': "Xalqaro Aloqalar Bo'limi",
    'office_name_en': "International Office",
    'slogan_uz': "Global Aloqalar, Mahalliy Muvaffaqiyat",
    'slogan_en': "Global Connections, Local Excellence",
    'email': "international@namdu.uz",
    'phone': "+998 69 210-01-35",
    'address_uz': "Namangan sh., Boburshox ko'chasi, 161-uy",
    'telegram': "https://t.me/namdu_uz",
    'facebook': "https://facebook.com/namdu.uz",
    'instagram': "https://instagram.com/namdu.uz",
    'youtube': "https://youtube.com/@namdu",
    'namdu_main_url': "https://namdu.uz",
})

StatCounter.objects.update_or_create(pk=1, defaults={
    'partner_universities': 47, 'partner_countries': 28,
    'exchange_students': 312, 'scopus_articles': 189,
    'active_grants': 32, 'visiting_professors': 24,
    'mou_agreements': 63, 'conferences_held': 18,
})

for i, (title, subtitle, btn1, url1, btn2, url2, color) in enumerate([
    ("Global Aloqalar,\nMahalliy Muvaffaqiyat",
     "Namangan davlat universiteti xalqaro hamkorlik, akademik mobillik va ilmiy tadqiqotlar orqali jahon ta'lim maydonida mustahkam o'rin egallaydi.",
     "Hamkorlar", "/partnerships/", "Yangiliklar", "/news/", "#000000"),
    ("47+ Hamkor Universitet\n28 Davlat bilan Aloqa",
     "QS, THE, WURI va GreenMetric reytinglarida ishtirok etuvchi, xalqaro miqyosda tan olingan universitetimiz.",
     "Reytinglar", "/rankings/", "Ilmiy faoliyat", "/research/", "#0a3d2e"),
    ("Akademik Mobillik\nErasmus+, DAAD va ko'proq",
     "312 dan ortiq talabamiz xorijda ta'lim olmoqda. Siz ham qo'shiling!",
     "Mobillik dasturlari", "/mobility/", "", "", "#1a0a3d"),
], 1):
    HeroSlide.objects.update_or_create(pk=i, defaults={
        'title_uz': title, 'subtitle_uz': subtitle,
        'btn_text_uz': btn1, 'btn_url': url1,
        'btn2_text_uz': btn2, 'btn2_url': url2,
        'overlay_color': color, 'overlay_opacity': 0.55,
        'media_type': 'image', 'order': i-1,
        'is_active': True, 'auto_play_duration': 5,
    })

for i, (title, desc, icon, url, color) in enumerate([
    ("Hemis OTM", "O'qituvchi va xodimlar", "ri-computer-line", "https://my.namdu.uz", "#1ab69d"),
    ("Erasmus+", "Mobillik dasturlari", "ri-flight-takeoff-line", "/mobility/", "#ee4a62"),
    ("Scopus", "Ilmiy nashrlar", "ri-article-line", "/research/", "#f8b81f"),
    ("Hisobotlar", "Yillik hisobotlar", "ri-file-pdf-line", "/reports/", "#534ab7"),
], 1):
    QuickLink.objects.update_or_create(pk=i, defaults={
        'title_uz': title, 'description_uz': desc,
        'icon_class': icon, 'url': url, 'color': color,
        'order': i, 'is_active': True,
    })

print("Core: OK")

# ===== NEWS =====
from apps.news.models import NewsCategory, News
from datetime import date

cats = {}
for pk, (name, slug, color) in enumerate([
    ("Shartnoma", "shartnoma", "#1ab69d"),
    ("Konferensiya", "konferensiya", "#1ba2db"),
    ("Mobillik", "mobillik", "#534ab7"),
    ("Mehmon professor", "mehmon-professor", "#ee4a62"),
], 1):
    obj, _ = NewsCategory.objects.update_or_create(pk=pk, defaults={'name_uz': name, 'slug': slug, 'color': color})
    cats[pk] = obj

news_data = [
    (1, cats[1], "Polsha Lodz texnologiya universiteti bilan MOU imzolandi", "polsha-lodz-mou-2025",
     "NamDU va Polsha Lodz texnologiya universiteti o'rtasida akademik hamkorlik memorandumi imzolandi.",
     "<p>Namangan davlat universiteti rektori va Polsha Lodz texnologiya universiteti vakillari o'rtasida ikki tomonlama akademik hamkorlik memorandumi imzolandi.</p><p>Hujjat quyidagilarni nazarda tutadi:</p><ul><li>Talabalar va o'qituvchilar almashinuvi dasturi</li><li>Qo'shma ilmiy tadqiqot loyihalari</li><li>Qo'shma konferensiyalar tashkil etish</li></ul>",
     date(2025, 5, 8), True, 420),
    (2, cats[2], "Xalqaro ilm-fan forumi 2025 — 18 davlatdan 340 ishtirokchi", "ilm-fan-forumi-2025",
     "NamDU da o'tkazilgan xalqaro ilmiy forum 18 davlatdan 340 dan ortiq olimlarni birlashtirdi.",
     "<p>2025 yil aprel oyida NamDU da o'tkazilgan <strong>Xalqaro Ilm-fan Forumi</strong> katta muvaffaqiyat bilan yakunlandi.</p><ul><li>Sun'iy intellekt va mashina o'rganish</li><li>Qishloq xo'jaligi texnologiyalari</li><li>Barqaror energetika yechimlari</li></ul><p>Jami 87 ta ilmiy maqola taqdim etildi.</p>",
     date(2025, 4, 22), False, 315),
    (3, cats[3], "12 talabamiz Erasmus+ dasturi doirasida Germaniyaga jo'nadi", "erasmus-germaniya-2025",
     "NamDU talabalarining guruhi Erasmus+ dasturi doirasida Germaniya universitetlarida o'qish uchun jo'nab ketdi.",
     "<p>2025 yil aprel oyida 12 nafar NamDU talabasi Erasmus+ dasturi doirasida Germaniyaga jo'nab ketdi.</p><ul><li>TU Berlin — 5 talaba (Kompyuter fanlari)</li><li>Heidelberg universiteti — 4 talaba (Kimyo)</li><li>Munich texnik universiteti — 3 talaba (Muhandislik)</li></ul>",
     date(2025, 4, 10), True, 280),
    (4, cats[4], "Prof. Hans Weber (TU Berlin) NamDU da sun'iy intellekt bo'yicha ma'ruzalar o'tkazdi", "prof-hans-weber-2025",
     "Berlin texnik universitetining professori Hans Weber NamDU da bir haftalik AI ma'ruzalar seriyasini o'tkazdi.",
     "<p>TU Berlin professori <strong>Dr. Hans Weber</strong> NamDU da sun'iy intellekt va chuqur o'rganish mavzusida haftalik intensiv kurs o'tkazdi.</p><ul><li>Deep Learning asoslari</li><li>Computer Vision amaliyoti</li><li>NLP — tabiiy til ishlash</li></ul><p>Kursda 150 dan ortiq talaba ishtirok etdi.</p>",
     date(2025, 4, 15), False, 198),
]

for pk, cat, title, slug, short_desc, body, pub_date, featured, views in news_data:
    News.objects.update_or_create(pk=pk, defaults={
        'category': cat, 'title_uz': title, 'slug': slug,
        'short_description_uz': short_desc, 'body_uz': body,
        'published_at': pub_date, 'is_published': True,
        'is_featured': featured, 'views': views,
    })

print("News: OK")

# ===== PARTNERSHIPS =====
from apps.partnerships.models import Country, Partner, MOU

countries = {}
for pk, (name, code) in enumerate([
    ("Germaniya", "DE"), ("Polsha", "PL"), ("Fransiya", "FR"),
    ("Xitoy", "CN"), ("Rossiya", "RU"), ("Turkiya", "TR"),
    ("Janubiy Koreya", "KR"), ("AQSH", "US"),
], 1):
    obj, _ = Country.objects.update_or_create(pk=pk, defaults={'name_uz': name, 'code': code})
    countries[pk] = obj

partners = {}
for pk, (name, short, country_pk, since) in enumerate([
    ("Technische Universität Berlin", "TU Berlin", 1, 2022),
    ("Lodz University of Technology", "Lodz Tech", 2, 2025),
    ("Université Paris-Saclay", "Paris-Saclay", 3, 2023),
    ("Zhejiang University", "Zhejiang Univ", 4, 2021),
    ("Ankara University", "Ankara Univ", 6, 2020),
    ("Korea University", "Korea Univ", 7, 2023),
], 1):
    obj, _ = Partner.objects.update_or_create(pk=pk, defaults={
        'name': name, 'short_name': short,
        'country': countries[country_pk],
        'partner_type': 'university',
        'partnership_since': since,
        'order': pk, 'is_active': True,
        'is_featured': pk <= 2,
    })
    partners[pk] = obj

for pk, (partner_pk, title, signed) in enumerate([
    (1, "Akademik hamkorlik va talabalar almashinuvi to'g'risida bitim", date(2022, 9, 15)),
    (2, "Qo'shma ilmiy tadqiqot va ta'lim dasturlari to'g'risida memorandum", date(2025, 5, 8)),
    (3, "Erasmus+ dasturi doirasida hamkorlik shartnomasi", date(2023, 3, 20)),
], 1):
    MOU.objects.update_or_create(pk=pk, defaults={
        'partner': partners[partner_pk],
        'title_uz': title,
        'signed_date': signed,
        'status': 'active',
    })

print("Partnerships: OK")

# ===== RESEARCH =====
from apps.research.models import ResearchArea, Publication, ResearchGrant

areas = {}
for pk, name in enumerate([
    "Nanomateriallar va fizika", "Qishloq xo'jaligi texnologiyalari",
    "Sun'iy intellekt va ML", "Suv resurslari va irrigatsiya"
], 1):
    obj, _ = ResearchArea.objects.update_or_create(pk=pk, defaults={'name_uz': name})
    areas[pk] = obj

for pk, (title, authors, journal, year, q, db, citations, area_pk, featured) in enumerate([
    ("Optical properties of nanocomposite ZnO films deposited by magnetron sputtering",
     "Karimov A.K., Yusupov M.T., Rashidov D.O., Weber H.", "Journal of Applied Physics", 2024, "Q1", "scopus", 14, 1, True),
    ("Machine learning approaches for agricultural yield prediction in Central Asia",
     "Toshmatov N.A., Kim S.H., Ismoilov B.R.", "Computers and Electronics in Agriculture", 2024, "Q2", "scopus", 8, 2, True),
    ("Water-saving drip irrigation systems for cotton farming in arid conditions",
     "Mirzayev S.U., Hasanov F.T., Park J.W.", "Agricultural Water Management", 2023, "Q1", "scopus", 22, 4, False),
    ("Deep learning for plant disease detection using hyperspectral imaging",
     "Nazarov D.I., Liu Y., Tursunov O.A.", "Remote Sensing", 2024, "Q1", "scopus", 6, 3, True),
], 1):
    Publication.objects.update_or_create(pk=pk, defaults={
        'title': title, 'authors': authors, 'journal': journal,
        'year': year, 'quartile': q, 'database': db,
        'citations': citations, 'research_area': areas[area_pk], 'is_featured': featured,
    })

for pk, (title, funder, amount, pi) in enumerate([
    ("Markaziy Osiyo uchun aqlli irrigatsiya tizimlarini ishlab chiqish", "European Commission (Horizon Europe)", "485000.00", "Prof. Mirzayev S.U."),
    ("O'zbekiston qishloq xo'jaligida AI qo'llash", "DAAD (Germany)", "120000.00", "Prof. Toshmatov N.A."),
    ("ZnO nano materiallar tadqiqoti", "Academy of Sciences of Uzbekistan", "45000.00", "Prof. Karimov A.K."),
], 1):
    ResearchGrant.objects.update_or_create(pk=pk, defaults={
        'title_uz': title, 'funder': funder, 'amount': amount,
        'start_date': date(2024, 1, 1), 'status': 'active',
        'principal_investigator': pi,
    })

print("Research: OK")

# ===== RANKINGS =====
from apps.rankings.models import RankingAgency, Ranking

agencies = {}
for pk, (name, short) in enumerate([
    ("Quacquarelli Symonds", "QS"),
    ("Times Higher Education", "THE"),
    ("World University Rankings for Innovation", "WURI"),
    ("UI GreenMetric", "GreenMetric"),
], 1):
    obj, _ = RankingAgency.objects.update_or_create(pk=pk, defaults={'name': name, 'short_name': short})
    agencies[pk] = obj

for pk, (agency_pk, name, year, position, score, featured) in enumerate([
    (1, "QS World University Rankings", 2025, "801-850", 18.4, True),
    (1, "QS Asia University Rankings", 2025, "351-400", 22.1, True),
    (2, "THE World University Rankings", 2025, "1001-1200", None, False),
    (2, "THE Impact Rankings — SDG 4", 2024, "201-300", None, True),
    (3, "WURI Global Ranking", 2024, "Top 500", None, False),
    (4, "UI GreenMetric World University Rankings", 2024, "201-300", 6850, True),
], 1):
    Ranking.objects.update_or_create(pk=pk, defaults={
        'agency': agencies[agency_pk], 'ranking_name': name,
        'year': year, 'position': position,
        'score': score, 'is_featured': featured,
    })

print("Rankings: OK")

# ===== SUSTAINABILITY =====
from apps.sustainability.models import SDGGoal, GreenMetric

for pk, (number, name, color, activities) in enumerate([
    (4, "Sifatli ta'lim", "#c5192d", "NamDU innovatsion ta'lim dasturlari va masofaviy ta'lim platformalari orqali sifatli ta'limni ta'minlaydi. THE Impact Rankings SDG-4 bo'yicha 201-300 o'rinni egallagan."),
    (5, "Gender tengligi", "#ff3a21", "NamDU da ayol talabalar va o'qituvchilar ulushi yil sayin o'smoqda. Gender tenglik dasturlari va stipendiyalar orqali qizlar ta'limini qo'llab-quvvatlaymiz."),
    (7, "Arzon va toza energiya", "#fcc30b", "Kampusda quyosh panellari o'rnatilgan. 2024 yilda energiya sarfi 38% ga kamaytirildi."),
    (9, "Sanoat, innovatsiya va infratuzilma", "#fd6925", "NamDU texnopark va startap akseleratori orqali innovatsion ekotizimni rivojlantirmoqda. 32 aktiv grant loyihasi."),
    (13, "Iqlim o'zgarishlariga qarshi kurash", "#3f7e44", "GreenMetric reytingida ishtirok etamiz. CO2 emissiyasi 18% ga kamaytirilib, 4200 daraxt ekildi."),
    (17, "Maqsadlar uchun sheriklik", "#19486a", "47+ hamkor universitet, 28 davlat, 63 MOU shartnoma. Global sheriklik orqali barcha SDG maqsadlarga erishishga intilamiz."),
], 1):
    SDGGoal.objects.update_or_create(pk=pk, defaults={
        'number': number, 'name_uz': name, 'color': color,
        'namdu_activities_uz': activities, 'is_active': True,
    })

for pk, (cat, value, unit, desc) in enumerate([
    ("co2", "-18", "%", "CO₂ qisqarish (2020-2024)"),
    ("trees", "4200", "", "Ekilgan daraxtlar"),
    ("recycling", "62", "%", "Qayta ishlash darajasi"),
    ("energy", "38", "%", "Energiya tejash"),
], 1):
    GreenMetric.objects.update_or_create(pk=pk, defaults={
        'category': cat, 'value': value, 'unit': unit,
        'description_uz': desc, 'year': 2024,
    })

print("Sustainability: OK")

# ===== MOBILITY =====
from apps.mobility.models import MobilityProgram

for pk, (name, ptype, host_pk, country_pk, months, funding, desc, deadline) in enumerate([
    ("Erasmus+ Student Exchange — TU Berlin", "erasmus", 1, 1, 6,
     "To'liq moliyalashtiriladi (stipendiya + uchish xarajatlari)",
     "Erasmus+ dasturi doirasida TU Berlin da bir semestr o'qish. Kompyuter fanlari, muhandislik va fizika yo'nalishlari uchun.",
     date(2025, 10, 1)),
    ("DAAD Research Fellowship", "daad", 1, 1, 12,
     "DAAD tomonidan to'liq moliyalashtiriladi",
     "Germaniyada 1 yillik ilmiy tadqiqot uchun DAAD stipendiyasi. Magistr va doktorantura talabalari uchun.",
     date(2025, 10, 15)),
    ("Erasmus+ — Paris-Saclay University", "erasmus", 3, 3, 6,
     "Qisman moliyalashtiriladi",
     "Fransiya Paris-Saclay universitetida Erasmus+ dasturi. Kimyo va biologiya yo'nalishlari.",
     date(2025, 11, 30)),
    ("Korea University Exchange Program", "other", 6, 7, 6,
     "Qisman — stipendiya bor",
     "Janubiy Koreya Korea universitetida almashinuv dasturi. Barcha yo'nalishlar uchun ochiq.",
     date(2025, 9, 15)),
], 1):
    MobilityProgram.objects.update_or_create(pk=pk, defaults={
        'name': name, 'program_type': ptype,
        'host_university': partners[host_pk],
        'host_country': countries[country_pk],
        'duration_months': months, 'funding': funding,
        'description_uz': desc, 'deadline': deadline,
        'is_active': True,
    })

print("Mobility: OK")

# ===== PROFESSORS =====
from apps.professors.models import VisitingProfessor

for pk, (name, title, host_pk, country_pk, spec, visit_start, visit_end, lecture, status, featured) in enumerate([
    ("Prof. Dr. Hans Weber", "Computer Science Department Chair", 1, 1,
     "Sun'iy intellekt, Deep Learning, Computer Vision",
     date(2025, 4, 8), date(2025, 4, 15),
     "Deep Learning va Computer Vision: nazariya va amaliyot", "past", True),
    ("Prof. Marie Dubois", "Associate Professor", 3, 3,
     "Kvant kimyosi, nanomateriallar",
     date(2025, 6, 1), date(2025, 6, 14),
     "Kvant kimyosi: yangi materiallar yaratishda qo'llanilishi", "upcoming", True),
    ("Prof. Kim Jae-won", "Professor of Agricultural Engineering", 6, 7,
     "Qishloq xo'jaligi muhandisligi, aqlli fermerlik",
     date(2025, 3, 10), date(2025, 3, 20),
     "Smart farming va IoT texnologiyalari qishloq xo'jaligida", "past", False),
], 1):
    VisitingProfessor.objects.update_or_create(pk=pk, defaults={
        'full_name': name, 'title': title,
        'home_university': partners[host_pk],
        'country': countries[country_pk],
        'specialization_uz': spec,
        'visit_start': visit_start, 'visit_end': visit_end,
        'lecture_topic_uz': lecture,
        'status': status, 'is_featured': featured,
    })

print("Professors: OK")

# ===== CONFERENCES =====
from apps.conferences.models import Conference

for pk, (title, slug, desc, start, end, location, fmt, participants, countries_n, reg_url, reg_deadline, featured) in enumerate([
    ("Xalqaro Ilm-fan va Innovatsiyalar Forumi 2025", "isif-2025",
     "<p>NamDU tomonidan tashkil etilgan <strong>Xalqaro Ilm-fan va Innovatsiyalar Forumi</strong> O'rta Osiyo mintaqasidagi eng yirik ilmiy tadbirlardan biriga aylandi.</p><p>Forum yo'nalishlari:</p><ul><li>Sun'iy intellekt va raqamli texnologiyalar</li><li>Barqaror qishloq xo'jaligi</li><li>Yashil energetika yechimlari</li></ul>",
     date(2025, 4, 22), date(2025, 4, 24), "NamDU Asosiy bino, Namangan",
     "hybrid", 340, 18, "", None, True),
    ("Raqamli Ta'lim Xalqaro Konferensiyasi 2025", "icde-2025",
     "<p>Ta'limda raqamli texnologiyalar va sun'iy intellektni qo'llash mavzusidagi xalqaro konferensiya.</p><ul><li>Online ta'lim platformalari samaradorligi</li><li>AI va adaptiv o'rganish tizimlari</li></ul>",
     date(2025, 9, 15), date(2025, 9, 16), "NamDU, Namangan (Hybrid)",
     "hybrid", 0, 0, "https://namdu.uz/conf2025", date(2025, 8, 30), False),
    ("Yosh Tadqiqotchilar Forumi — NamDU 2025", "yrf-namdu-2025",
     "<p>Yosh olimlar va tadqiqotchilar uchun maxsus platforma — o'z ishlarini xalqaro auditoriyaga taqdim etish imkoniyati.</p>",
     date(2025, 11, 20), date(2025, 11, 21), "NamDU, Namangan",
     "offline", 0, 0, "", date(2025, 10, 31), False),
], 1):
    Conference.objects.update_or_create(pk=pk, defaults={
        'title_uz': title, 'slug': slug, 'description_uz': desc,
        'start_date': start, 'end_date': end, 'location_uz': location,
        'format': fmt, 'participants_count': participants,
        'countries_count': countries_n, 'registration_url': reg_url,
        'registration_deadline': reg_deadline,
        'is_active': True, 'is_featured': featured,
    })

print("Conferences: OK")

# ===== COMMUNITY =====
from apps.community.models import CommunityProject

for pk, (title, desc, start, end, benef, location, sdg, active, featured) in enumerate([
    ("'Ko'k O'rikzor' — Namangan bog'larini tiklash loyihasi",
     "<p>NamDU talabalari va o'qituvchilari birgalikda Namangan shahrida 2000 dan ortiq mevali daraxt ko'chatlarini ekdi.</p>",
     date(2024, 3, 1), date(2024, 11, 30), 5000,
     "Namangan shahar, Bog'ishamol tumani", "SDG 13, SDG 11, SDG 15", False, True),
    ("Qishloq maktablariga raqamli ta'lim — 'DigiSchool'",
     "<p>Namangan viloyatining 15 ta qishloq maktabiga kompyuter va internet ulanishi ta'minlandi, o'qituvchilar uchun raqamli savodxonlik kurslari o'tkazildi.</p>",
     date(2024, 9, 1), None, 3200,
     "Namangan viloyati, 15 ta qishloq maktabi", "SDG 4, SDG 9", True, True),
    ("Yoshlar innovatsiya akseleratori — StartUp NamDU",
     "<p>NamDU texnopark bazasida yosh tadqiqotchilar va talabalar uchun startap akseleratori ishga tushirildi. 12 ta startap tanlandi.</p>",
     date(2025, 1, 15), None, 120,
     "NamDU Texnopark", "SDG 8, SDG 9, SDG 17", True, False),
], 1):
    CommunityProject.objects.update_or_create(pk=pk, defaults={
        'title_uz': title, 'description_uz': desc,
        'start_date': start, 'end_date': end,
        'beneficiaries': benef, 'location_uz': location,
        'sdg_connection': sdg, 'is_active': active, 'is_featured': featured,
    })

print("Community: OK")

# ===== REPORTS =====
from apps.reports.models import AnnualReport

for pk, (title, rtype, year, desc, pages) in enumerate([
    ("Xalqaro Aloqalar Bo'limi Yillik Hisoboti 2024", "annual", 2024,
     "NamDU Xalqaro aloqalar bo'limining 2024 yilgi faoliyati to'g'risida to'liq hisobot.", 48),
    ("Barqarorlik va SDG Hisoboti 2024", "sustainability", 2024,
     "GreenMetric va THE Impact Rankings uchun asosiy manba hujjat. Yashil kampus ko'rsatkichlari.", 36),
    ("Ilmiy Faoliyat Hisoboti 2024", "research", 2024,
     "Scopus nashrlar, grantlar, patentlar va xalqaro hamkorlik tadqiqotlari statistikasi.", 28),
    ("Akademik Mobillik Hisoboti 2023-2024", "mobility", 2024,
     "Erasmus+, DAAD va boshqa dasturlar bo'yicha almashinuv talabalari statistikasi.", 22),
], 1):
    AnnualReport.objects.update_or_create(pk=pk, defaults={
        'title_uz': title, 'report_type': rtype, 'year': year,
        'description_uz': desc, 'pages': pages, 'is_public': True,
    })

print("Reports: OK")
print("\n✅ Barcha ma'lumotlar muvaffaqiyatli yuklandi!")