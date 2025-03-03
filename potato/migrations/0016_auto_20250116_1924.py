# Generated by Django 3.2.25 on 2025-01-17 01:24

from django.db import migrations, models
import django.db.models.deletion
import potato.FHIR_DataTypes.FHIR_primitive


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0015_auto_20250116_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='code_cc',
            field=models.ManyToManyField(blank=True, limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-timing-abbreviation.html'}, related_name='timing_code_cc', to='potato.FHIR_GP_Coding'),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='code_text',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_StringField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_bounds_duration',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='potato.fhir_gp_quantity_duration'),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_bounds_period',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='potato.fhir_gp_period'),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_bounds_range',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='potato.fhir_gp_range'),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_count',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_PositiveIntField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_count_max',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_PositiveIntField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_day_of_week',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_CodeField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_duration',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DecimalField(blank=True, decimal_places=17, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_duration_max',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DecimalField(blank=True, decimal_places=17, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_duration_unit',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_CodeField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_frequency',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_PositiveIntField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_frequency_max',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_PositiveIntField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_offset',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_UnsignedIntField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_period',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DecimalField(blank=True, decimal_places=17, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_period_max',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DecimalField(blank=True, decimal_places=17, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_period_unit',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_CodeField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_time_of_day',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fhir_gp_timing',
            name='repeat_when',
            field=potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_CodeField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='FHIR_GP_Timing_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', potato.FHIR_DataTypes.FHIR_primitive.FHIR_primitive_DateTimeField(blank=True, null=True)),
                ('timing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='potato.fhir_gp_timing')),
            ],
        ),
    ]
