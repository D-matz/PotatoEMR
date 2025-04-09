# Generated by Django 5.2 on 2025-04-09 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='category_codes',
            field=models.ManyToManyField(blank=True, limit_choices_to={'codings__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-category.html'}, related_name='allergyintolerance_category', to='potato.fhir_gp_coding'),
        ),
        migrations.AlterField(
            model_name='fhir_allergyintolerance',
            name='criticality_code',
            field=models.ForeignKey(blank=True, limit_choices_to={'codings__binding_rule': 'https://www.hl7.org/fhir/valueset-allergy-intolerance-criticality.html'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allergyintolerance_criticality', to='potato.fhir_gp_coding'),
        ),
        migrations.RemoveField(
            model_name='fhir_allergyintolerance_reaction',
            name='severity',
        ),
        migrations.AddField(
            model_name='fhir_allergyintolerance_reaction',
            name='severity',
            field=models.ForeignKey(blank=True, limit_choices_to={'codings__binding_rule': 'https://www.hl7.org/fhir/valueset-reaction-event-severity.html'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reaction_severity', to='potato.fhir_gp_coding'),
        ),
    ]
