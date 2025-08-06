from django import forms
from django.utils.translation import gettext_lazy as _
from settlement.models import LegalGuardiant, Patient, Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address', 'zip_code', 'city']
        labels = {
            'address': _('Address'),
            'zip_code': _('Zip Code'),
            'city': _('City'),
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Street address')}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Zip code')}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('City')}),
        }


class LegalGuardianForm(forms.ModelForm):
    class Meta:
        model = LegalGuardiant
        fields = ['first_name', 'last_name', 'display_name']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'display_name': _('Display Name'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('First name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last name')}),
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Display name')}),
        }

    def clean_display_name(self):
        display_name = self.cleaned_data['display_name']
        if not display_name:
            first_name = self.cleaned_data.get('first_name', '')
            last_name = self.cleaned_data.get('last_name', '')
            display_name = f"{first_name} {last_name}".strip()
        return display_name


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'display_name', 'social_insurance_number', 'legalGuardiant']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'display_name': _('Display Name'),
            'social_insurance_number': _('Social Insurance Number'),
            'legalGuardiant': _('Legal Guardian'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('First name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last name')}),
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Display name')}),
            'social_insurance_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Social insurance number')}),
            'legalGuardiant': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['legalGuardiant'].queryset = LegalGuardiant.objects.all()
        self.fields['legalGuardiant'].empty_label = _('Select a legal guardian')

    def clean_display_name(self):
        display_name = self.cleaned_data['display_name']
        if not display_name:
            first_name = self.cleaned_data.get('first_name', '')
            last_name = self.cleaned_data.get('last_name', '')
            display_name = f"{first_name} {last_name}".strip()
        return display_name