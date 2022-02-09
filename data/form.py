from django import forms
from .models import SaleForm
from .models import RentForm
from .models import Contact


class Sale(forms.ModelForm):
    class Meta:
        model = SaleForm
        fields = ('types', 'dist', 'thaluk', 'add', 'name',
                  'phone', 'email', 'amt', 'desc', 'image', 'video')


class Rent(forms.ModelForm):
    class Meta:
        model = RentForm
        fields = ('types', 'dist', 'thaluk', 'add', 'name', 'phone',
                  'email', 'amt', 'bed', 'door', 'desc', 'image', 'video')


class Contacts(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('username', 'phone', 'email', 'desc')
