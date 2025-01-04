# Generated by Django 3.2.25 on 2025-01-04 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0004_auto_20250103_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='FHIR_GP_Quantity_Age',
            fields=[
                ('fhir_gp_quantity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='potato.fhir_gp_quantity')),
            ],
            bases=('potato.fhir_gp_quantity',),
        ),
    ]
