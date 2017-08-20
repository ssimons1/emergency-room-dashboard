# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    NAME = (
        ('N', 'Neuro'),
        ('C', 'Cardio'),
        ('T', 'Trauma'),
        ('E', 'ENT'),
        ('GS', 'General Surgery'),
        ('M', 'Maternity'),
        ('O', 'Oncology'),
        ('U', 'Urology'),
    )
    department_name = models.CharField(max_length=2, choices=NAME, primary_key=True)

class Patient(models.Model):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    PRIORITY = (
        ('1', 'Critical'),
        ('2', 'Serious'),
        ('3', 'Minor'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    priority = models.CharField(max_length=1, choices=PRIORITY)
    being_seen = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    injury_description = models.CharField(max_length=400)
    allergies = models.CharField(max_length=150)

class Doctor(models.Model):
    TITLE = (
        ('Doctor', 'Dr.'),
    )
    title = models.CharField(max_length=6, choices=TITLE)
    first_initial = models.CharField(max_length=4)
    last_name = models.CharField(max_length=30)
    occupied = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    time_finish_shift = models.TimeField('Time finished shift')

class Nurse(models.Model):
    TITLE = (
        ('doctor', 'Dr.'),
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('miss', 'Miss'),
    )
    title = models.CharField(max_length=6, choices=TITLE)
    first_initial = models.CharField(max_length=4)
    last_name = models.CharField(max_length=30)
    occupied = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    time_finish_shift = models.TimeField('Time finished shift')

