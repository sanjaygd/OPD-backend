# Generated by Django 4.2 on 2023-04-27 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0006_rename_visted_patientvisit_visited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvisit',
            old_name='patient_name',
            new_name='patient',
        ),
    ]
