from django import forms
from .models import Modelmodule12

class Module12Form(forms.ModelForm):

    class Meta:
        model = Modelmodule12
        fields = ['consecuencias','refiere']
        widgets = {
            'consecuencias': forms.TextInput(attrs={'class':'form-control'}),
            'refiere': forms.TextInput(attrs={'class':'form-control'}),
        }
