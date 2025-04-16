# Generated by Django 5.2 on 2025-04-16 03:25

import potato.models_dir.FHIR_DataTypes.FHIR_primitive
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fhir_encounter',
            name='plannedEndDate',
            field=potato.models_dir.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fhir_encounter',
            name='plannedStartDate',
            field=potato.models_dir.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField(blank=True, null=True),
        ),
    ]
