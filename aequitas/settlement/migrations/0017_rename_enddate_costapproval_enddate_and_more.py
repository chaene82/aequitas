# Generated by Django 4.2.7 on 2023-11-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0016_patient_social_insurance_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costapproval',
            old_name='EndDate',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='settlement',
            old_name='EndDate',
            new_name='endDate',
        ),
        migrations.AddField(
            model_name='costapproval',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='settlement',
            name='receivedAmount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='settlement',
            name='requestetAmount',
            field=models.FloatField(null=True),
        ),
    ]
