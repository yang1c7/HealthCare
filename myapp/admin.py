from django.contrib import admin
from django.db import models
from .models import Patient, Doctor, Topic

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Topic)

