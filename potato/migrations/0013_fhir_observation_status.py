# Generated by Django 3.2.25 on 2025-01-13 04:28

from django.db import migrations
import potato.FHIR_DataTypes.FHIR_primitive


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0012_auto_20250112_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='fhir_observation',
            name='status',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_CodeField(choices=[('registered', 'Registered'), ('preliminary', 'Preliminary'), ('final', 'Final'), ('amended', 'Amended'), ('corrected', 'Corrected'), ('cancelled', 'Cancelled'), ('entered-in-error', 'Entered in Error'), ('unknown', 'Unknown')], default='unknown', max_length=20),
        ),
    ]
