from rest_framework_json_api import serializers
from .models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'display_name')

