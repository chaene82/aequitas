from django.test import TestCase
from settlement.models import Patient

# Create your tests here.

class TestSettlement(TestCase):
    """
    This are general test cases for the Aequtias model Treatments.
    """

    def test_setup(self):

        self.assertEqual(1, 1)


    def test_patient_add(self):
        """Test adding a customer
        create a patient and count the number of the patient.
        """
        a = Patient(display_name = "Test Patient", address = "Test Address")
        a.save()

        nr_patient = Patient.objects.count()
        print("Number of Records = ", nr_patient)
        self.assertEqual(nr_patient, 1)





    