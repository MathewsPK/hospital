# Generated by Django 4.2.6 on 2023-10-15 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_appointment_appointments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='p_dep',
        ),
    ]
