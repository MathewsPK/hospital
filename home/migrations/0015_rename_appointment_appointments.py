# Generated by Django 4.2.6 on 2023-10-14 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_appointment_p_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appointment',
            new_name='appointments',
        ),
    ]
