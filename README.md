# IT Support System

Django веб-қосымшасы: IT-қолдау өтінімдерін тіркеу және басқару.

## Мүмкіндіктер
- Өтінімдер тізімі
- Жаңа өтінім қосу
- Өтінімді өзгерту және жою
- Басымдық пен мәртебені көрсету
- INFO және WARNING журналдары
- SQLite (жергілікті) және PostgreSQL (Render) қолдауы

## Жергілікті іске қосу (Windows PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Команда шығарған кілтті `.env` ішіндегі `SECRET_KEY=` жолына қойыңыз.

```powershell
python manage.py migrate
python manage.py runserver
```

Браузер: http://127.0.0.1:8000/

## GitHub
`.env` файлын GitHub-қа жүктемеңіз. `.gitignore` оны жасырады.
GitHub репозиторийіне `manage.py`, `config/`, `tickets/`, `requirements.txt`, `build.sh`, `.env.example`, `README.md` жүктеңіз.

## Render
- Runtime: Python 3
- Build Command: `bash build.sh`
- Start Command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

Environment Variables:
- `SECRET_KEY`: жаңа құпия кілт
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: Render домені, мысалы `your-service.onrender.com` (https:// және / жазылмайды)
- `DATABASE_URL`: Render PostgreSQL Internal Database URL

Render PostgreSQL дерекқорын Web Service-пен бір аймақта жасаңыз және Internal Database URL қолданыңыз.
