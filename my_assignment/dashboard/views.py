# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from dashboard.forms import PatientForm, DoctorForm, NurseForm
from dashboard.models import Patient, Doctor, Nurse, Department

# Create your views here.
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

        elif doctor_form:
            if doctor_form.is_valid():
                doctor = doctor_form.save(commit=False)
                doctor.save()
                return redirect('/restricted')

        elif nurse_form:
            if nurse_form.is_valid():
                nurse = nurse_form.save(commit=False)
                nurse.save()
                return redirect('restricted')

    else:
        patient_form = PatientForm()
        doctor_form = DoctorForm()
        nurse_form = NurseForm()

    context = {"patients": patients,
               "doctors": doctors,
               "nurses": nurses,
               "patient_form": patient_form,
               "doctor_form": doctor_form,
               "nurse_form": nurse_form}

    return render(request, "restricted.html", context)
