# Generated by Django 4.0.2 on 2023-01-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0002_remove_patient_diagnosis_patient_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalCuardiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('display_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('zip_code', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
