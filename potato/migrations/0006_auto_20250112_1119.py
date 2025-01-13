# Generated by Django 3.2.25 on 2025-01-12 17:19

from django.db import migrations, models
import django.db.models.deletion
import potato.FHIR_DataTypes.FHIR_primitive


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0005_auto_20250112_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fhir_allergyintolerance',
            old_name='category_cc',
            new_name='category_codes',
        ),
        migrations.RemoveField(
            model_name='fhir_allergyintolerance',
            name='criticality_cc',
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='clinical_status_cctext',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_StringField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='code_cc',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergyintolerance-code.html'}, related_name='allergyintolerance_code', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='criticality_code',
            field=models.ForeignKey(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-criticality.html'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='potato.fhir_gp_coding'),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance',
            name='verification_status_cctext',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_StringField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance_participant',
            name='function_cc',
            field=models.ManyToManyField(limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-participation-role-type.html'}, related_name='allergyintolerance_participant_function', to='potato.FHIR_GP_Coding'),
        ),
        migrations.DeleteModel(
            name='FHIR_AllergyIntolerance_CategoryThrough',
        ),
    ]
