from rest_framework_json_api import serializers
import datetime
from .models import Patient, CostApproval, Address, LegalGuardiant, Insurance, PaymentMethode, CostApprovalType, Settlement


class CostApprovalTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CostApprovalType
        fields = ('name', 'templateForm')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'zip_code', 'city')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'display_name', 'legalGuardiant', 'address')
        
class LegalGuardiantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LegalGuardiant
        fields = ('first_name', 'last_name', 'display_name', 'address')

class CostApprovalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CostApproval
        fields = ('name', 'ca_type', 'patient')

class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance
        fields = ('name', 'insurance_type', 'address')

class PaymentMethodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethode
        fields = ('name', 'pm_type', 'bank', 'city', 'IBAN', 'beneficjent')
        
class SettlementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settlement
        fields = ('name', 'costApproval', 'status', 'startDate', 'EndDate', 'invoiceDate', 'paymentDate')
        
    def create(self, validated_data):
        validated_data['invoiceDate'] = datetime.datetime.now()
        print(validated_data['name'])
        return Settlement(**validated_data)
        
