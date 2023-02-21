from django.shortcuts import render
from .models import Patient, CostApproval, Address, LegalGuardiant, Insurance, PaymentMethode,\
    CostApprovalType, Settlement
from .serializers import PatientSerializer, CostApprovalSerializer, AddressSerializer,\
    LegalGuardiantSerializer, InsuranceSerializer, PaymentMethodeSerializer, CostApprovalTypeSerializer, \
        SettlementSerializer
from rest_framework import viewsets

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