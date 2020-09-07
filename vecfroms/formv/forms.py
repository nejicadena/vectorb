from django import forms

points = [
    ('0', 'Nunca'),
    ('1', 'Alguna vez al año o menos'),
    ('2', 'Una vez al mes o menos'),
    ('3', 'Algunas veces o menos'),
    ('4', 'Una vez a la semana'),
    ('5', 'Varias veces a la semana'),
    ('6', 'Diariamente'),
]
acepted = [
    ('0', 'He leído este formulario de consentimiento y acepto participar en el taller “Estrategias de acción ante el burnout”'),
    ('1','No acepto dar mi consentimiento y rechazo participar en el taller “Estrategias de acción ante el burnout”')
]

class ContactForm(forms.Form):
    
    age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    state = forms.CharField( required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    n_hijos = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control'}) )
    lugar = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    profesion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    especialidad = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    time_ex = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    work = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    service = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    sick = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    who = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class FormBornout(forms.Form):
    
    que1 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que2 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que3 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que4 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que5 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que6 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que7 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que8 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que9 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que10 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que11 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que12 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que13 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que14 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que15 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que16 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que17 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que18 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que19 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que20 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que21 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    que22 = forms.ChoiceField(choices=points, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))

class FormConsent(forms.Form):
    acepted = forms.ChoiceField(choices=acepted,widget=forms.RadioSelect(attrs={'class':'form-check-input'}))