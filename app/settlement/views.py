from django.shortcuts import render
from .models import Patient, CostApproval, Address, LegalGuardian, Insurance, PaymentMethod,\
    CostApprovalType, Settlement
from .serializers import PatientSerializer, CostApprovalSerializer, AddressSerializer,\
    LegalGuardianSerializer, InsuranceSerializer, PaymentMethodSerializer, CostApprovalTypeSerializer, \
        SettlementSerializer
from rest_framework import viewsets
from fillpdf import fillpdfs

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

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class LegalGuardianViewSet(viewsets.ModelViewSet):
    queryset = LegalGuardian.objects.all()
    serializer_class = LegalGuardianSerializer

class CostApprovalViewSet(viewsets.ModelViewSet):
    queryset = CostApproval.objects.all()
    serializer_class = CostApprovalSerializer
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    
class SettlementViewSet(viewsets.ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer