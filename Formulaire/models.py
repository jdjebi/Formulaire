from django.db import models
from django.utils.translation import gettext as _

class Patient(models.Model):

    SEXE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),   
    ]

    # Information générale
    nom_patient = models.CharField(_("Nom patient"),max_length=255,blank=True,null=True)
    date_creation = models.DateField(_("Date de création"), auto_now=True, auto_now_add=False,blank=True,null=True)
    date_creation_str = models.CharField(_("Date de creation (STR)"),max_length=255,blank=True,null=True) # Date sans contrainte de format
    sexe = models.CharField(_("Sexe"),choices=SEXE,max_length=255,blank=True,null=True)
    date_naissance = models.DateField(_("Date de naissance"),blank=True,null=True)
    date_naissance_str = models.CharField(_("Date de naissance (STR)"),max_length=255,blank=True,null=True) # Date sans contrainte de format
    poids = models.FloatField(_("Poids"),blank=True,null=True)
    taille = models.FloatField(_("Taille"),blank=True,null=True)
    
    # Pression artérielle
    pa_systotique = models.FloatField(_("PA systolique"),blank=True,null=True)
    pa_diastolique =  models.FloatField(_("PA diastolique"),blank=True,null=True)
    pam = models.FloatField(_("PAM"),blank=True,null=True)
    rythme_cardiaque_pa = models.FloatField(_("Rythme Cardiaque (PA)"),blank=True,null=True)
    hta = models.FloatField(_("HTA"),blank=True,null=True)

    # Oxymétrie
    oxymetrie = models.FloatField(_("Oxymétrie"),blank=True,null=True)
    rythme_cardiaque_oxy =  models.FloatField(_("Rythme Cardiaque (Oxy)"),blank=True,null=True)

    # Température
    temperature = models.FloatField(_("Température"),blank=True,null=True)

    # Indince de masse corporelle
    imc = models.FloatField(_("IMC"),blank=True,null=True)
    interpretation_imc = models.CharField(_("Interprétation IMC"),max_length=255,blank=True,null=True)

    # Les interprétations
    gyclémie_1 = models.FloatField(_("Glycémie (mg/dl)"),blank=True,null=True)
    gyclémie_2 = models.FloatField(_("Glycémie (mmol/L)"),blank=True,null=True)
    diabete = models.CharField(_("Diabète"),max_length=255,blank=True,null=True)
    cardiopathie = models.CharField(_("Cardiopathie"),max_length=255,blank=True,null=True)
    ecg = models.CharField(_("ECG"),max_length=255,blank=True,null=True)
    interpretation_ecg = models.CharField(_("interprétations ECG"),max_length=255,blank=True,null=True)

    # Evaluation COVID-19
    vulnerabilite = models.IntegerField(_("Vulnérabilité"),blank=True,null=True)
    groupe_risque = models.IntegerField(_("Groupe de risque d'exposition"),blank=True,null=True)
    score_risque = models.IntegerField(_("Score de risque IMC"),blank=True,null=True)

