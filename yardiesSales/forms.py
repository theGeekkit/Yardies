from django import forms
from .models import SaleLocation

class CreateSaleLocationForm(forms.ModelForm):
    class Meta:
        model = SaleLocation
    fields = ['state','city', 'street']   