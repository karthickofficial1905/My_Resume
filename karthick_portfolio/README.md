# Karthick R - Portfolio Website (Django)

## Setup Instructions

### 1. Install Django
```
pip install django
```

### 2. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User (optional - to view contact messages)
```
python manage.py createsuperuser
```

### 4. Run the Server
```
python manage.py runserver
```

### 5. Open in Browser
```
http://127.0.0.1:8000
```
Admin panel: http://127.0.0.1:8000/admin

## Project Structure
```
karthick_portfolio/
├── manage.py
├── requirements.txt
├── karthick_portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio/
    ├── models.py        # ContactMessage model
    ├── views.py         # Home & Contact views
    ├── urls.py
    ├── admin.py
    ├── templates/portfolio/
    │   └── index.html   # Main HTML template
    └── static/
        ├── css/style.css
        └── js/main.js
```

## Features
- Dark theme portfolio (Mukesh V style)
- About Me, Skills, Projects, Experience, Contact sections
- Contact form with database storage
- Django Admin panel to view messages
- Mobile responsive
- Smooth scroll navigation
