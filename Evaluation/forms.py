from django import forms
from .models import Evaluation

class Distrbution(forms.ModelForm):
    class Meta:
        model= Evaluation
        fields=['id_doctor_fk']
#, 'id_doctor_fk2', 'id_doctor_fk3'

        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 
        
