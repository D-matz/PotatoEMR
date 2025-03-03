# Generated by Django 3.2.25 on 2025-01-12 16:21

from django.db import migrations, models
import potato.FHIR_DataTypes.FHIR_primitive


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0003_auto_20250111_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='category',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-category.html'}, related_name='allergyintolerance_category', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='criticality',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-criticality.html'}, related_name='allergyintolerance_criticality', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='type',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html'}, related_name='allergyintolerance_type', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='verification_status',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html'}, related_name='allergyintolerance_verificationstatus', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_gp_identifier',
            name='type',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-identifier-type.html'}, related_name='identifier_type', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_patient',
            name='marital_status',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-marital-status.html'}, related_name='patient_maritalstatus', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_patient',
            name='marital_status_text',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_StringField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='clinical_status',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html'}, related_name='allergyintolerance_clinicalstatus', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AlterField(
            model_name='fhir_gp_coding',
            name='binding',
            field=models.ManyToManyField(related_name='bindings', to='potato.FHIR_GP_Binding'),
        ),
    ]
