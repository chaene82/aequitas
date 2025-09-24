# Generated manually - refactoring model names and field names

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0017_rename_enddate_costapproval_enddate_and_more'),
    ]

    operations = [
        # Rename model from PaymentMethode to PaymentMethod
        migrations.RenameModel(
            old_name='PaymentMethode',
            new_name='PaymentMethod',
        ),
        
        # Rename model from LegalGuardiant to LegalGuardian  
        migrations.RenameModel(
            old_name='LegalGuardiant',
            new_name='LegalGuardian',
        ),

        # Rename fields to snake_case conventions
        migrations.RenameField(
            model_name='LegalGuardian',
            old_name='create',
            new_name='created',
        ),
        
        migrations.RenameField(
            model_name='Patient',
            old_name='create',
            new_name='created',
        ),
        
        migrations.RenameField(
            model_name='Patient',
            old_name='legalGuardiant',
            new_name='legal_guardian',
        ),
        
        migrations.RenameField(
            model_name='PaymentMethod',
            old_name='create',
            new_name='created',
        ),
        
        migrations.RenameField(
            model_name='PaymentMethod',
            old_name='beneficjent',
            new_name='beneficiary',
        ),
        
        migrations.RenameField(
            model_name='Insurance',
            old_name='create',
            new_name='created',
        ),
        
        migrations.RenameField(
            model_name='CostApprovalType',
            old_name='templateForm',
            new_name='template_form',
        ),
        
        migrations.RenameField(
            model_name='CostApproval',
            old_name='create',
            new_name='created',
        ),
        
        migrations.RenameField(
            model_name='CostApproval',
            old_name='paymentMethode',
            new_name='payment_method',
        ),
        
        migrations.RenameField(
            model_name='CostApproval',
            old_name='refCode',
            new_name='ref_code',
        ),
        
        migrations.RenameField(
            model_name='CostApproval',
            old_name='startDate',
            new_name='start_date',
        ),
        
        migrations.RenameField(
            model_name='CostApproval',
            old_name='endDate',
            new_name='end_date',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='create',
            new_name='created',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='costApproval',
            new_name='cost_approval',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='startDate',
            new_name='start_date',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='endDate',
            new_name='end_date',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='requestetAmount',
            new_name='requested_amount',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='receivedAmount',
            new_name='received_amount',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='invoiceDate',
            new_name='invoice_date',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='paymentDate',
            new_name='payment_date',
        ),
        
        migrations.RenameField(
            model_name='Settlement',
            old_name='documentPath',
            new_name='document_path',
        ),
    ]