from django import forms
from .models import Projects
class Add_Idea(forms.ModelForm):
    class Meta:
        model =Projects
        fields=['name_projects','filled_projects','descriotion_projects']

        widgets ={
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            #'id_projects':forms.NumberInput(attrs={'class':'form-control'}),
        } 