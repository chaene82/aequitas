# Generated by Django 4.1.6 on 2023-02-20 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0011_remove_insurance_city_remove_insurance_zip_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='type',
            new_name='insurance_type',
        ),
    ]
