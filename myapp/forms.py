from django import forms
from myapp.models import Patient, Doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        first_name = forms.CharField(required=False)
        last_name = forms.CharField(required=False)
        age = forms.CharField(required=False)
        gender = forms.CharField(required=False)
        address = forms.CharField(required=False)
        user_id = forms.CharField(required=False)
        symptom = forms.CharField(required=False)
        fields = {'first_name', 'last_name', 'age', 'gender', 'address', 'user_id', 'symptom'}


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = {'name', 'patient', 'diagnosis', 'treatment'}


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
