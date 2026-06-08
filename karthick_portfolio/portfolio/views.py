from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def index(request):
    context = {
        'skills': {
            'Frontend': ['HTML', 'CSS', 'JavaScript', 'Responsive Design'],
            'Backend': ['Python', 'Django', 'Django ORM'],
            'Database': ['SQLite', 'MySQL', 'CRUD Operations'],
        },
        'projects': [
            {
                'num': '01',
                'name': 'Spartans Mobile E-Commerce',
                'desc': 'Real-time e-commerce web app with product management, cart, orders & live deployment on PythonAnywhere.',
                'tags': ['Django', 'Python', 'HTML/CSS'],
                'url': 'https://spartansmobiles.pythonanywhere.com',
            },
            {
                'num': '02',
                'name': 'HR & Admin Dashboard',
                'desc': 'Full-featured admin system with employee management, attendance tracking, payroll, pie charts & complaint ticketing.',
                'tags': ['Django', 'Python', 'Charts', 'SQLite'],
                'url': '#',
            },
            {
                'num': '03',
                'name': 'Positivus — Static Website',
                'desc': 'Responsive marketing website built with HTML, CSS & JavaScript. Source available on GitHub.',
                'tags': ['HTML', 'CSS', 'JavaScript'],
                'url': 'https://github.com/karthick-gmk/positivus',
            },
        ],
        'experience': [
            {
                'role': 'Python Developer Intern',
                'company': 'Adhoc Softwares Private Limited',
                'period': 'Jan 2026 – April 2026',
                'location': 'Coimbatore, Tamil Nadu',
                'desc': [
                    'Developed and maintained robust backend logic using the Django framework.',
                    'Created responsive user interfaces utilizing HTML, CSS, and minimal JavaScript.',
                    'Successfully engineered and deployed "Spartans-mobile," a real-time e-commerce web application.',
                    'Worked on Login & Registration, Admin & Employee Management, E-commerce, Invoice & Bill Printing, Currency & Tax Conversion, HR Dashboards, Pie Charts, and Support Ticket Systems.',
                ],
                'tags': ['Django', 'Python', 'HTML', 'CSS', 'JavaScript', 'SQLite'],
            }
        ],
    }
    return render(request, 'portfolio/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            # DB la save pannurom
            ContactMessage.objects.create(
                name=name, email=email,
                subject=subject, message=message
            )
            # Email anuthurom (console la print aagum development la)
            try:
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=f"From: {name} <{email}>\n\n{message}",
                    from_email=settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'noreply@portfolio.com',
                    recipient_list=['karthickofficial1905@gmail.com'],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, 'Message sent successfully! I will get back to you soon.')
        else:
            messages.error(request, 'Please fill all fields.')

    return redirect('/#contact')
