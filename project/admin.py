## Register the models with the Django Admin tool
# project/admin.py
from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile)
admin.site.register(PersonalMessage)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(GroupMessage)


