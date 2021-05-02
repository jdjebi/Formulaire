# Generated by Django 3.2 on 2021-05-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_patient', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom patient')),
                ('date_creation', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de création')),
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=255, null=True, verbose_name='Sexe')),
                ('date_naissance', models.DateTimeField(blank=True, null=True, verbose_name='Date de naissance')),
                ('poids', models.FloatField(blank=True, null=True, verbose_name='Poids')),
                ('taille', models.FloatField(blank=True, null=True, verbose_name='Taille')),
                ('pa_systotique', models.FloatField(blank=True, null=True, verbose_name='PA systolique')),
                ('pa_diastolique', models.FloatField(blank=True, null=True, verbose_name='PA diastolique')),
                ('pam', models.FloatField(blank=True, null=True, verbose_name='PAM')),
                ('rythme_cardiaque_pa', models.FloatField(blank=True, null=True, verbose_name='Rythme Cardiaque (PA)')),
                ('hta', models.FloatField(blank=True, null=True, verbose_name='Rythme Cardiaque (PA)')),
                ('oxymetrie', models.FloatField(blank=True, null=True, verbose_name='Oxymétrie')),
                ('rythme_cardiaque_oxy', models.FloatField(blank=True, null=True, verbose_name='Rythme Cardiaque (Oxy)')),
                ('temperature', models.FloatField(blank=True, null=True, verbose_name='Température')),
                ('imc', models.FloatField(blank=True, null=True, verbose_name='IMC')),
                ('interpretation_imc', models.FloatField(blank=True, null=True, verbose_name='Interprétation IMC')),
                ('gyclémie_1', models.FloatField(blank=True, null=True, verbose_name='Glycémie (mg/dl)')),
                ('gyclémie_2', models.FloatField(blank=True, null=True, verbose_name='Glycémie (mmol/L)')),
                ('diabete', models.CharField(blank=True, max_length=255, null=True, verbose_name='Diabète')),
                ('cardiopathie', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cardiopathie')),
                ('ecg', models.CharField(blank=True, max_length=255, null=True, verbose_name='ECG')),
                ('interpretation_ecg', models.CharField(blank=True, max_length=255, null=True, verbose_name='interprétations ECG')),
                ('vulnerabilite', models.IntegerField(blank=True, null=True, verbose_name='Vulnérabilité')),
                ('groupe_risque', models.IntegerField(blank=True, null=True, verbose_name="Groupe de risque d'exposition")),
                ('score_risque', models.IntegerField(blank=True, null=True, verbose_name='Score de risque IMC')),
            ],
        ),
    ]
