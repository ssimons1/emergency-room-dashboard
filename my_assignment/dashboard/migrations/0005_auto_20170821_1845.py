# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20170821_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Neuro', 'Neuro'), ('Cardio', 'Cardio'), ('Trauma', 'Trauma'), ('ENT', 'ENT'), ('General Surgery', 'General Surgery'), ('Maternity', 'Maternity'), ('Oncology', 'Oncology'), ('Urology', 'Urology')], max_length=15, primary_key=True, serialize=False),
        ),
    ]
