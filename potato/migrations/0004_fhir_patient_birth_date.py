# Generated by Django 3.2.25 on 2024-12-28 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0003_alter_fhir_gp_humanname_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='fhir_patient',
            name='birth_date',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_birthDate', to='potato.fhir_primitive_datefield'),
        ),
    ]