# Generated by Django 4.2 on 2023-04-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0004_remove_patientvisit_dob_remove_patientvisit_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvisit',
            old_name='patent_name',
            new_name='patient_name',
        ),
    ]
