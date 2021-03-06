# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from dashboard.datasets import doctors_unavailable_available, nurses_unavailable_available, department_patients
from dashboard.forms import PatientForm, DoctorForm, NurseForm
from dashboard.models import Patient, Doctor, Nurse, Department
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# Homepage with public dashboard


# Login page
def submit_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        if user.is_active:
            return redirect('/restricted')
        else:
            return redirect('/login')
    else:
        return redirect('/login')


# Logout page
def logout(request):
    auth.logout(request)
    return redirect('/')


# Restricted dashboard which will open once successfully logged in

@login_required
def restricted(request):
    patients = Patient.objects.order_by('last_name')
    doctors = Doctor.objects.order_by('last_name')
    nurses = Nurse.objects.order_by('last_name')

    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        nurse_form = NurseForm(request.POST)

        if patient_form:
            if patient_form.is_valid():
                patient = patient_form.save(commit=False)
                patient.save()
                return redirect('/restricted')

        if doctor_form:
            if doctor_form.is_valid():
                doctor = doctor_form.save(commit=False)
                doctor.save()
                return redirect('/restricted')

        if nurse_form:
            if nurse_form.is_valid():
                nurse = nurse_form.save(commit=False)
                nurse.save()
                return redirect('/restricted')

    else:
        patient_form = PatientForm()
        doctor_form = DoctorForm()
        nurse_form = NurseForm()

    context = {"patients": patients,
               "doctors": doctors,
               "nurses": nurses,
               "patient_form": patient_form,
               "doctor_form": doctor_form,
               "nurse_form": nurse_form,
               }

    return render(request, "restricted.html", context)


def dashboard(request):
    patients = Patient.objects.order_by('last_name')
    context = {"doctor_data": doctors_unavailable_available(),
               "nurse_data": nurses_unavailable_available(),
               "patients": patients,
               "department_data": department_patients(),
               }

    return render(request, "homepage.html", context)





