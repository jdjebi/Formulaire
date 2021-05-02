from django.contrib import admin
from django.urls import path
from Formulaire.views import *

urlpatterns = [
    path('',patients_list,name="patients.list"),
    path('patients/<int:id>',patients_show,name="patients.show"),
    path('patients/create',patients_create,name="patients.create"),
    path('patients/import',patients_import,name="patients.import"),
    path('patients/export',patients_export,name="patients.export"),
    path('admin/', admin.site.urls),
]
