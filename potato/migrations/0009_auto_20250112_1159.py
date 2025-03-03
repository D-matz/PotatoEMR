# Generated by Django 3.2.25 on 2025-01-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0008_auto_20250112_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='category_codes',
            field=models.ManyToManyField(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-category.html'}, related_name='allergyintolerance_category', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='clinical_status_cc',
            field=models.ManyToManyField(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html'}, related_name='allergyintolerance_clinicalstatus', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='code_cc',
            field=models.ManyToManyField(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergyintolerance-code.html'}, related_name='allergyintolerance_code', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='type_cc',
            field=models.ManyToManyField(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html'}, related_name='allergyintolerance_type', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='verification_status_cc',
            field=models.ManyToManyField(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html'}, related_name='allergyintolerance_verificationstatus', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance_reaction',
            name='severity',
            field=models.ForeignKey(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-reaction-event-severity.html'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allergyintolerance_reaction_severity', to='potato.fhir_gp_coding'),
        ),
    ]
