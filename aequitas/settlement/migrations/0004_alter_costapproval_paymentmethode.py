# Generated by Django 4.1.6 on 2023-02-17 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0003_rename_payment_paymentmethode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costapproval',
            name='paymentMethode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CostApproval_paymentMethode', to='settlement.paymentmethode'),
        ),
    ]
