from django import forms
from .models import Modelmodule12, Modelmodule14

class Module12Form(forms.ModelForm):

    class Meta:
        model = Modelmodule12
        fields = ['consecuencias','refiere']
        widgets = {
            'consecuencias': forms.TextInput(attrs={'class':'form-control'}),
            'refiere': forms.TextInput(attrs={'class':'form-control'}),
        }

class Module14Form(forms.ModelForm):

    class Meta:
        model = Modelmodule14
        fields = ['nancy']
        widgets = {
            'nancy': forms.TextInput(attrs={'class':'form-control'}),
          
        }

