from django import forms
from myapp.models import Patient, Doctor


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = {'name', 'age', 'gender', 'symptom'}

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = {'name', 'patient', 'diagnosis', 'treatment'}



