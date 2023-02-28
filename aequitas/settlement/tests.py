from django.test import TestCase
import os, datetime
from settlement.models import Patient, LegalGuardiant, Address
from settlement.views import Invoice

# Create your tests here.

test_address = {
    'address'       : 'Teststrasse 1',
    'zip_code'       : '1234',
    'city'          : 'Testhausen',
}

test_patient = {
    'first_name'    : 'Test',
    'last_name'     : 'Patient',
    'display_name'  : 'Test Patient',
    
}

class TestSettlement(TestCase):
    """
    This are general test cases for the Aequtias model Treatments.
    """
    #fixtures = ['test/testdata_settlement.json']


    def test_setup(self):

        self.assertEqual(1, 1)

    def test_address(self):

        a = Address(**test_address)
        a.save()
        
        nr_address = Address.objects.count()
        print("Number of Records = ", nr_address)
        self.assertEqual(nr_address, 1)
        
        
    def test_legal_guardiant_add(self):
        """Test adding a customer
        create a patient and count the number of the patient.
        """
        addr = Address(**test_address)
        addr.save()
        
        a = LegalGuardiant(display_name = "Test Guardiant", address = addr)
        a.save()
        
        nr_lg = LegalGuardiant.objects.count()
        print("Number of Records (LG) = ", nr_lg)
        self.assertEqual(nr_lg, 1)

    def test_patient_add(self):
        """Test adding a customer
        create a patient and count the number of the patient.
        """
        #a = Patient(display_name = "Test Patient")
        a = Patient(**test_patient)
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
        self.assertEqual(os.path.getsize('test/documents/' + document), os.path.getsize('documents/test_hle.pdf'))
        
    def test_create_hle_invoice(self):
        
        # Create test Setup
        address = Address(**test_address)
        address.save()
        test_patient['address'] = address
        #patient = Patient(**test_patient)
        #patient.save()
        
        dt_now = datetime.datetime.now()
        seq = int(dt_now.strftime("%Y%m%d%H%M%S"))
        
        template = 'Rechnung+HE+318.632.2_D+2023_r.pdf'
        document = 'test_create_hle_invoice_' + str(seq) + '.pdf'
        
        i = Invoice(template, document)    
        i.forms_path = 'forms/'
        i.document_path = 'test/documents/'
        
        nr_patient = Patient.objects.count()
        print("HLE Number of Records = ", nr_patient)
        self.assertEqual(nr_patient, 1)                

        
           
        
        
        
        
        





    