from django import forms
from .models import Produit

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields='__all__'
