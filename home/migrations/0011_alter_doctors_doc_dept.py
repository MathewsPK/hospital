# Generated by Django 4.2.6 on 2023-10-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_doctors_doc_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_dept',
            field=models.CharField(default='Nil', max_length=100),
        ),
    ]
