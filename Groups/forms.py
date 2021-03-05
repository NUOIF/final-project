
from django import forms
from .models import Groups


class CRN(forms.ModelForm):
    class Meta:
        model= Groups
        fields=['id_groups','name_groups']


        widgets ={
            'id_groups':forms.Select(attrs={'class':'form-control'}),
            'name_Groups':forms.TextInput(attrs={'class':'form-control'}),
        } 
