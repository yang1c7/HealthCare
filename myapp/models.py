from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    symptom = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    patient = models.ForeignKey(Patient, related_name='patients', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    diagnosis = models.TextField(max_length=300, null=True, blank=True)
    treatment = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.name

