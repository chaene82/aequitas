from rest_framework_json_api import serializers
import datetime
from .models import Patient, CostApproval, Address, LegalGuardian, Insurance, PaymentMethod, CostApprovalType, Settlement


class CostApprovalTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CostApprovalType
        fields = ('name', 'template_form')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'zip_code', 'city')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'display_name', 'legal_guardian', 'address')
        
class LegalGuardianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LegalGuardian
        fields = ('first_name', 'last_name', 'display_name', 'address')

class CostApprovalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CostApproval
        fields = ('name', 'ca_type', 'patient')

class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance
        fields = ('name', 'insurance_type', 'address')

class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('name', 'pm_type', 'bank', 'city', 'IBAN', 'beneficiary')
        
class SettlementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settlement
        fields = ('name', 'cost_approval', 'status', 'start_date', 'end_date', 'invoice_date', 'payment_date')
        
    def create(self, validated_data):
        validated_data['invoice_date'] = datetime.datetime.now()
        print(validated_data['name'])
        return Settlement(**validated_data)
        
