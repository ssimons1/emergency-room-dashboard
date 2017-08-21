from django import forms
from dashboard.models import Patient, Doctor, Nurse


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'priority', 'department', 'room_number', 'injury_description', 'allergies']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['title', 'first_initial', 'last_name', 'occupied', 'department', 'time_finish_shift']


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['title', 'first_initial', 'last_name', 'occupied', 'department', 'time_finish_shift']

