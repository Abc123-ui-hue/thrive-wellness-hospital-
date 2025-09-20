import os
import sys
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from django import forms
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

BASE_DIR = os.path.dirname(__file__)

# ---------------- SETTINGS ----------------
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="thrive-clinic-secret",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        MIDDLEWARE=[
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ],
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            __name__,
        ],
        TEMPLATES=[{
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {"context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]},
        }],
        DATABASES={"default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }},
        STATIC_URL="/static/",
    )

# ---------------- MODELS ----------------
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} - {self.date} {self.time}"

# ---------------- FORMS ----------------
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["date", "time", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

# ---------------- VIEWS ----------------
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.patient = request.user
            appt.save()
            return redirect("my_appointments")
    else:
        form = AppointmentForm()
    return render(request, "book.html", {"form": form})

@login_required
def my_appointments(request):
    appts = Appointment.objects.filter(patient=request.user).order_by("-date", "-time")
    return render(request, "my_appointments.html", {"appointments": appts})

# ---------------- URLS ----------------
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("book/", book_appointment, name="book"),
    path("my/", my_appointments, name="my_appointments"),
]

# ---------------- ADMIN ----------------
from django.contrib import admin
admin.site.register(Appointment)

# ---------------- INLINE TEMPLATES ----------------
TEMPLATES_DIR = os.path.join(BASE_DIR, __name__)
os.makedirs(os.path.join(TEMPLATES_DIR, "templates"), exist_ok=True)
settings.TEMPLATES[0]["DIRS"] = [os.path.join(TEMPLATES_DIR, "templates")]

def write_template(name, content):
    path = os.path.join(TEMPLATES_DIR, "templates", name)
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(content)

# Base template
write_template("base.html", """ 
<!DOCTYPE html>
<html>
<head>
  <title>Thrive Clinic</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container">
    <a class="navbar-brand" href="/">Thrive Clinic</a>
    <div>
      <a class="nav-link d-inline text-white" href="/">Home</a>
      {% if user.is_authenticated %}
        <a class="nav-link d-inline text-white" href="/book/">Book</a>
        <a class="nav-link d-inline text-white" href="/my/">My Appointments</a>
        <a class="nav-link d-inline text-white" href="/logout/">Logout</a>
      {% else %}
        <a class="nav-link d-inline text-white" href="/login/">Login</a>
        <a class="nav-link d-inline text-white" href="/register/">Register</a>
      {% endif %}
    </div>
  </div>
</nav>
<div class="container mt-4">
  {% block content %}{% endblock %}
</div>
</body>
</html>
""")

# Home
write_template("home.html", """ 
{% extends "base.html" %}
{% block content %}
<div class="p-5 mb-4 bg-light rounded-3">
  <h1 class="display-4">Welcome to Thrive Mental Wellness Clinic</h1>
  <p class="lead">Your mental health is our priority.</p>
</div>
{% endblock %}
""")

# Register
write_template("register.html", """ 
{% extends "base.html" %}
{% block content %}
<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button class="btn btn-success">Register</button>
</form>
{% endblock %}
""")

# Login
write_template("login.html", """ 
{% extends "base.html" %}
{% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button class="btn btn-primary">Login</button>
</form>
{% endblock %}
""")

# Book
write_template("book.html", """ 
{% extends "base.html" %}
{% block content %}
<h2>Book Appointment</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button class="btn btn-primary">Book</button>
</form>
{% endblock %}
""")

# My Appointments
write_template("my_appointments.html", """ 
{% extends "base.html" %}
{% block content %}
<h2>My Appointments</h2>
<table class="table table-striped">
  <tr><th>Date</th><th>Time</th><th>Notes</th></tr>
  {% for a in appointments %}
  <tr><td>{{ a.date }}</td><td>{{ a.time }}</td><td>{{ a.notes }}</td></tr>
  {% empty %}
  <tr><td colspan="3">No appointments yet.</td></tr>
  {% endfor %}
</table>
<a class="btn btn-success" href="/book/">Book New</a>
{% endblock %}
""")

# ---------------- RUN ----------------
if __name__ == "__main__":
    import django
    from django.core.management import execute_from_command_line
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    django.setup()
    execute_from_command_line(sys.argv)
