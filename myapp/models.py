from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    user_id = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=200, blank=True)
    symptom = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return "username: {}, first_name:{},last_name: {}, age:{}, gender:{}, address:{}"\
            .format(self.username, self.first_name, self.last_name, self.age, self.gender, self.address)


class Doctor(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    user_id = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "username: {}, first_name:{},last_name: {}, age:{}, gender:{}, address:{}" \
            .format(self.username, self.first_name, self.last_name, self.age, self.gender, self.address)


class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.name

