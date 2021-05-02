from django.contrib import admin
from Formulaire.models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id","nom_patient",)