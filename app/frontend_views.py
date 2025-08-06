from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db import transaction
from forms import LegalGuardianForm, PatientForm, AddressForm


def home_view(request):
    """Home page view."""
    return render(request, 'home.html')


def login_view(request):
    """Custom login view."""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _('Welcome back, {}!').format(user.username))
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, _('Invalid username or password.'))
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})


@login_required
def create_legal_guardian_view(request):
    """Create a new legal guardian with address."""
    if request.method == 'POST':
        legal_guardian_form = LegalGuardianForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if legal_guardian_form.is_valid() and address_form.is_valid():
            try:
                with transaction.atomic():
                    # Save address first
                    address = address_form.save()
                    
                    # Save legal guardian with address
                    legal_guardian = legal_guardian_form.save(commit=False)
                    legal_guardian.address = address
                    legal_guardian.save()
                    
                    messages.success(
                        request, 
                        _('Legal Guardian "{}" has been created successfully.').format(legal_guardian.display_name)
                    )
                    return redirect('create_legal_guardian')
            except Exception as e:
                messages.error(request, _('An error occurred while saving the legal guardian.'))
        else:
            messages.error(request, _('Please correct the errors below.'))
    else:
        legal_guardian_form = LegalGuardianForm()
        address_form = AddressForm()
    
    return render(request, 'create_legal_guardian.html', {
        'legal_guardian_form': legal_guardian_form,
        'address_form': address_form,
    })


@login_required
def create_patient_view(request):
    """Create a new patient with address."""
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if patient_form.is_valid() and address_form.is_valid():
            try:
                with transaction.atomic():
                    # Save address first
                    address = address_form.save()
                    
                    # Save patient with address
                    patient = patient_form.save(commit=False)
                    patient.address = address
                    patient.save()
                    
                    messages.success(
                        request, 
                        _('Patient "{}" has been created successfully.').format(patient.display_name)
                    )
                    return redirect('create_patient')
            except Exception as e:
                messages.error(request, _('An error occurred while saving the patient.'))
        else:
            messages.error(request, _('Please correct the errors below.'))
    else:
        patient_form = PatientForm()
        address_form = AddressForm()
    
    return render(request, 'create_patient.html', {
        'patient_form': patient_form,
        'address_form': address_form,
    })