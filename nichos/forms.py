from django import forms
from nichos.models import Reservation, Propietario

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Propietario

        fields = [
            'nombre',
            'dpi',
            'telefono',
            'direccion',
        ]

        labels = {

            'nombre': 'Nombre',
            'dpi': 'DPI',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'dpi':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
        }



    

