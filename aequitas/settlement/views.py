from django.shortcuts import render
from .models import Patient, CostApproval, Address, LegalGuardiant, Insurance, PaymentMethode,\
    CostApprovalType, Settlement
from .serializers import PatientSerializer, CostApprovalSerializer, AddressSerializer,\
    LegalGuardiantSerializer, InsuranceSerializer, PaymentMethodeSerializer, CostApprovalTypeSerializer, \
        SettlementSerializer
from rest_framework import viewsets

from fillpdf import fillpdfs


#fileds = fillpdfs.get_form_fields("../forms/Rechnung+HE+318.632.2_D+2023_r.pdf")
#fileds['11AHVNr'] = '1234'

#fillpdfs.write_fillable_pdf("../forms/Rechnung+HE+318.632.2_D+2023_r.pdf", '../documents/new.pdf', fileds)

#p = Patient(display_name = "Test Patient", address = "Test Address")

class Invoice:
    template = ''
    document = ''
    forms_path = '../forms/'
    document_path = '../documents/'
    filed = ''

    def __init__(self, template, document):
        self.template = template
        self.document = document
        
    def create(self, fields):
        template_file_path = self.forms_path + self.template
        document_file_path = self.document_path + self.document

        fillpdfs.write_fillable_pdf(template_file_path , document_file_path, fields)

        return document_file_path
    
    def get_fields(self):
        template_file_path = self.forms_path + self.template
        fileds = fillpdfs.get_form_fields(template_file_path)
        return fileds
        

        
    def hle(self, Patient, LegalGuardiant, CostApproval, PaymentMethode):
        return None
        
    


class CostApprovalTypeViewSet(viewsets.ModelViewSet):
    queryset = CostApprovalType.objects.all()
    serializer_class = CostApprovalTypeSerializer

class PaymentMethodeViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethode.objects.all()
    serializer_class = PaymentMethodeSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class LegalGuardiantViewSet(viewsets.ModelViewSet):
    queryset = LegalGuardiant.objects.all()
    serializer_class = LegalGuardiantSerializer

class CostApprovalViewSet(viewsets.ModelViewSet):
    queryset = CostApproval.objects.all()
    serializer_class = CostApprovalSerializer
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    
class SettelmentViewSet(viewsets.ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer