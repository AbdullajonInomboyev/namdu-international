# NamDU Xalqaro Bo'lim Sayti

NamDU asosiy saytining (namdu.uz) dizaynida qurilgan Xalqaro bo'lim sayti.
Django 4.2 + PostgreSQL + Jazzmin Admin

---

## O'rnatish (Local)

### 1. Talablar
- Python 3.10+
- PostgreSQL 14+
- pip

### 2. Loyihani klonlash va muhit yaratish

```bash
cd namdu_international
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 3. PostgreSQL ma'lumotlar bazasi yaratish

```sql
CREATE DATABASE namdu_international;
CREATE USER namdu_user WITH PASSWORD 'strong_password';
GRANT ALL PRIVILEGES ON DATABASE namdu_international TO namdu_user;
```

### 4. .env fayli yaratish

```bash
cp .env.example .env
```

`.env` faylini tahrirlang:
```
DEBUG=True
SECRET_KEY=django-insecure-SIZNING-SECRET-KEY
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=namdu_international
DB_USER=namdu_user
DB_PASSWORD=strong_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Migrate va superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 6. Ishga tushirish

```bash
python manage.py runserver
```

Sayt: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

---

## Loyiha tuzilmasi

```
namdu_international/
├── config/
│   ├── settings.py          # Asosiy sozlamalar
│   └── urls.py              # URL marshrutlash
├── apps/
│   ├── core/                # Sayt sozlamalari, statistika, hero
│   ├── news/                # 01 — Xalqaro yangiliklar
│   ├── rankings/            # 02 — Reytinglar
│   ├── sustainability/      # 03 — SDG va barqarorlik
│   ├── research/            # 04 — Ilmiy nashrlar, grantlar
│   ├── partnerships/        # 05 — Hamkor universitetlar, MOU
│   ├── mobility/            # 06 — Akademik mobillik (Erasmus+)
│   ├── students/            # 07 — Xalqaro talabalar
│   ├── professors/          # 08 — Mehmon professorlar
│   ├── conferences/         # 09 — Konferensiyalar
│   ├── community/           # 10 — Jamoaviy loyihalar
│   └── reports/             # 11 — Hisobotlar va siyosat
├── templates/               # HTML shablonlar
├── static/
│   ├── css/namdu.css        # namdu.uz rang va stillaridan nusxa
│   └── js/namdu.js          # JavaScript
├── media/                   # Yuklanган fayllar
├── locale/                  # UZ / RU / EN tarjimalar
├── requirements.txt
└── manage.py
```

## Admin panel bo'limlari

| App | Nima boshqariladi |
|-----|-------------------|
| **Core** | Sayt sozlamalari, statistika raqamlar, hero slaydlar, tez havolalar |
| **News** | Yangiliklar va kategoriyalar |
| **Rankings** | Reyting agentliklari va reytinglar |
| **Sustainability** | SDG maqsadlar, Green ko'rsatkichlar |
| **Research** | Nashrlar (Scopus), grantlar |
| **Partnerships** | Davlatlar, hamkor universitetlar, MOU shartnomalari |
| **Mobility** | Mobillik dasturlari, almashinuv talabalari |
| **Students** | Xalqaro talabalar, davlat bo'yicha statistika |
| **Professors** | Mehmon professorlar |
| **Conferences** | Konferensiyalar va tadbirlar |
| **Community** | Jamoaviy loyihalar |
| **Reports** | Hisobotlar va PDF fayllar |

## Til qo'shish
```bash
python manage.py makemessages -l uz
python manage.py makemessages -l ru
python manage.py makemessages -l en
python manage.py compilemessages
```

## Production (server)
```bash
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

Gunicorn + Nginx yoki uWSGI ishlatish tavsiya etiladi.
