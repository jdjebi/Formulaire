# Generated by Django 3.2 on 2021-05-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulaire', '0002_auto_20210502_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gyclémie_2',
            field=models.FloatField(blank=True, null=True, verbose_name='Glycémie (mmol/L)'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gyclémie_1',
            field=models.FloatField(blank=True, null=True, verbose_name='Glycémie (mg/dl)'),
        ),
    ]
