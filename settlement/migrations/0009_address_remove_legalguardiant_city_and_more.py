# Generated by Django 4.1.6 on 2023-02-20 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0008_rename_type_costapproval_ca_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, null=True)),
                ('zip_code', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='legalguardiant',
            name='city',
        ),
        migrations.RemoveField(
            model_name='legalguardiant',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='legalguardiant',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LegalGuardiant_Address', to='settlement.address'),
        ),
    ]