# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170821_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Neuro', 'Neuro'), ('Cardio', 'Cardio'), ('Trauma', 'Trauma'), ('ENT', 'ENT'), ('General Surgery', 'General Surgery'), ('Maternity', 'Maternity'), ('Oncology', 'Oncology'), ('Urology', 'Urology')], max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='title',
            field=models.CharField(choices=[('Dr.', 'Dr.')], max_length=6),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='title',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss')], max_length=6),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1),
        ),
    ]
