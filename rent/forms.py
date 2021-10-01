from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *

# House forms

class HouseModelForm(forms.ModelForm):
    class Meta:
        model = House
        fields = (
            'house_name',
            'tenant',
            'summary',
            'caretaker',
        )


class HouseForm(forms.Form):
    house_name = forms.CharField()
    tenant = forms.CharField()
    summary = forms.CharField()
    Caretaker = forms.CharField()


# Caretaker form

class CaretakerModelForm(forms.ModelForm):
    class Meta:
        model = Caretaker
        fields = (
            'name',
        )


class CaretakerForm(forms.Form):
    name = forms.CharField()

# Rent forms

class RentModelForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_entry',
        )


class RentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField()
    status = forms.CharField()


# Tenant forms
class TenantModelForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = (
            'house_name',
            'tenant',
            'summary',
            'caretaker',
        )


class TenantForm(forms.Form):
    house_name = forms.CharField()
    tenant = forms.CharField()
    summary = forms.CharField()
    Caretaker = forms.CharField()