# Generated by Django 3.2.25 on 2025-01-04 00:46

from django.db import migrations
import potato.FHIR_DataTypes.FHIR_primitive


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fhir_gp_annotation',
            name='time_datetime_precision',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField_Precision(blank=True, choices=[('year', 'Year'), ('month', 'Month'), ('day', 'Day'), ('seconds', 'Seconds')], default='day', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='fhir_gp_attachment',
            name='time_datetime_precision',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField_Precision(blank=True, choices=[('year', 'Year'), ('month', 'Month'), ('day', 'Day'), ('seconds', 'Seconds')], default='day', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='fhir_gp_period',
            name='end_datetime_precision',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField_Precision(blank=True, choices=[('year', 'Year'), ('month', 'Month'), ('day', 'Day'), ('seconds', 'Seconds')], default='day', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='fhir_gp_period',
            name='start_datetime_precision',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField_Precision(blank=True, choices=[('year', 'Year'), ('month', 'Month'), ('day', 'Day'), ('seconds', 'Seconds')], default='day', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='fhir_patient',
            name='birthDate_datetime_precision',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField_Precision(blank=True, choices=[('year', 'Year'), ('month', 'Month'), ('day', 'Day'), ('seconds', 'Seconds')], default='day', max_length=7, null=True),
        ),
    ]
