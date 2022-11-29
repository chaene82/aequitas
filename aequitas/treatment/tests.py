from django.test import TestCase, Client
from treatment.models import Institute


# Create your tests here.
class TestTreatment(TestCase):
    """
    This are general test cases for the Aequtias model Treatments.
    """



    def test_setup(self):

        self.assertEqual(1, 1)


    def test_institute(self):
        """
        create an institute and count the number of the institutes.
        """
        a = Institute(title = "Test Institute", address = "Test Address")
        a.save()

        nr_institute = Institute.objects.count()
        print("Number of Recors = ", nr_institute)
        self.assertEqual(nr_institute, 1)





    