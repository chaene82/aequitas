# Generated by Django 4.1.6 on 2023-02-20 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0010_remove_patient_city_remove_patient_zip_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='city',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='insurance',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Insurance_Address', to='settlement.address'),
        ),
    ]