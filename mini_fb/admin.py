## Register the models with the Django Admin tool
# mini_fb/admin.py
from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)