# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    NAME = (
        ('Neuro', 'Neuro'),
        ('Cardio', 'Cardio'),
        ('Trauma', 'Trauma'),
        ('ENT', 'ENT'),
        ('General Surgery', 'General Surgery'),
        ('Maternity', 'Maternity'),
        ('Oncology', 'Oncology'),
        ('Urology', 'Urology'),
    )
    department_name = models.CharField(max_length=15, choices=NAME, primary_key=True)

    def __str__(self):
        return self.department_name


class Patient(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
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
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room_number = models.IntegerField(blank=True, null=True)
    injury_description = models.CharField(max_length=400)
    allergies = models.CharField(max_length=150)

    def __str__(self):
        return self.last_name + ", " + self.first_name

class Doctor(models.Model):
    TITLE = (
        ('Dr.', 'Dr.'),
    )
    title = models.CharField(max_length=6, choices=TITLE)
    first_initial = models.CharField(max_length=4)
    last_name = models.CharField(max_length=30)
    occupied = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    time_finish_shift = models.TimeField('Time finished shift')

    def __str__(self):
        return self.title + " " + self.first_initial + " " + self.last_name

class Nurse(models.Model):
    TITLE = (
        ('Dr.', 'Dr.'),
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
    )
    title = models.CharField(max_length=6, choices=TITLE)
    first_initial = models.CharField(max_length=4)
    last_name = models.CharField(max_length=30)
    occupied = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    time_finish_shift = models.TimeField('Time finished shift')

    def __str__(self):
        return self.title + " " + self.first_initial + " " + self.last_name



