from django.test import TestCase
import os, datetime
from settlement.models import Patient, LegalGuardiant
from settlement.views import Invoice

# Create your tests here.

class TestSettlement(TestCase):
    """
    This are general test cases for the Aequtias model Treatments.
    """
    #fixtures = ['test/testdata_settlement.json']


    def test_setup(self):

        self.assertEqual(1, 1)
        
    def test_legal_guardiant_add(self):
        """Test adding a customer
        create a patient and count the number of the patient.
        """
        a = LegalGuardiant(display_name = "Test Guardiant")
        a.save()

    def test_patient_add(self):
        """Test adding a customer
        create a patient and count the number of the patient.
        """
        a = Patient(display_name = "Test Patient")
        a.save()

        nr_patient = Patient.objects.count()
        print("Number of Records = ", nr_patient)
        self.assertEqual(nr_patient, 1)
    
    
class TestInvoice(TestCase):     
    def test_create_invoice(self):
        dt_now = datetime.datetime.now()
        seq = int(dt_now.strftime("%Y%m%d%H%M%S"))
        
        template = 'Rechnung+HE+318.632.2_D+2023_r.pdf'
        document = 'test_create_invoice_' + str(seq) + '.pdf'
        
        i = Invoice(template, document)
        i.forms_path = 'forms/'
        i.document_path = 'test/documents/'
        fields = i.get_fields()
        
        fields['11AHVNr'] = '1234'
        result = i.create(fields)
              
        self.assertTrue(os.path.exists('test/documents/' + document))
        
        
        
        
        





    