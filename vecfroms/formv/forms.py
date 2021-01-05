from django import forms
from .models import ModelValid

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
ages = [
    (25, '18 a 30 años'),
    (35, '31 a 40 años'),
    (41, '41 a 50 años'),
    (55, '50 a 60 años'),
    (65, '61 años o más'),
]
estado_civil = [
    ('Soltera', 'Soltera (o)'),
    ('Divorciada', 'Divorciada (o)'),
    ('Casada', 'Casada (o)'),
    ('En unión libre', 'En unión libre'),
]
recidencia = [
    ('Aguascalientes', 'Aguascalientes'),('Baja California', 'Baja California'),('Baja California Sur', 'Baja California Sur'),
    ('Chiapas', 'Chiapas'),('Chihuahua', 'Chihuahua'),('Coahuila', 'Coahuila'),('Colima', 'Colima'),
    ('CDMX', 'CDMX'),('Durango', 'Durango'),('Estado de México', 'Estado de México'),('Guanajuato', 'Guanajuato'),
    ('Guerrero', 'Guerrero'),('Hidalgo', 'Hidalgo'),('Jalisco', 'Jalisco'),('Michoacán', 'Michoacán'),
    ('Morelos', 'Morelos'),('Nayarit', 'Nayarit'),('Nuevo León', 'Nuevo León'),('Oaxacae', 'Oaxaca'),
    ('Puebla', 'Puebla'),('Querétaro', 'Querétaro'),('Quintana Roo', 'Quintana Roo'),('San Luis Potosí', 'San Luis Potosí'),
    ('Sinaloa', 'Sinaloa'),('Sonora', 'Sonora'),('Tabasco', 'Tabasco'),('Tamaulipas', 'Tamaulipas'),
    ('Tlaxcala', 'Tlaxcala'),('Veracruz', 'Veracruz'),('Yucatán', 'Yucatán'),('Zacatecas', 'Zacatecas'),
]
profes = [
    ('Enfermeria', 'Enfermería (auxiliar, técnico, licenciatura)'),
    ('Laboratorista clínico', 'Laboratorista clínico'),
    ('Medicina', 'Medicina'),
    ('Odontología', 'Odontología'),
    ('Psicología', 'Psicología'),
    ('Psiquiatría', 'Psiquiatría'),
    ('Trabajo Social', 'Trabajo Social'),
]
yes_or_not = [
    ('si','Si'),
    ('no','No')
]
experenciatime = [
    (5,'0 a 5 años'),
    (10,'6 a 10 años'),
    (15,'11 a 15 años'),
    (20,'16 a 20 años'),
    (25,'21 a 25 años'),
    (30,'26 a 30 años'),
    (35,'31 a 35 años'),
    (40,'36 a 40 años'),
    (50,'Más de 41 años'),
]
# experenciatime = [
#     ('0 a 5 años','0 a 5 años'),
#     ('6 a 10 años','6 a 10 años'),
#     ('11 a 15 años','11 a 15 años'),
#     ('16 a 20 años','16 a 20 años'),
#     ('21 a 25 años','21 a 25 años'),
#     ('26 a 30 años','26 a 30 años'),
#     ('31 a 35 años','31 a 35 años'),
#     ('36 a 40 años','36 a 40 años'),
#     ('Más de 41 años','Más de 41 años'),
# ]
servicomedico = [
    ('Alergia e inmunologia','Alergia e inmunologia'),  ('Anestesiología','Anestesiología'),  ('Angiología','Angiología'),  ('Cardiología','Cardiología'),
    ('Cirugía Cardiovascular','Cirugía Cardiovascular'),  ('Cirugía General','Cirugía General'),  ('Cirugía Maxilofacial','Cirugía Maxilofacial'),  ('Cirugía Pediatra','Cirugía Pediatra'),
    ('Cirugia Plastica y Reconstructiva','Cirugia Plastica y Reconstructiva'),  ('Dermatología','Dermatología'),  ('Endocrinología','Endocrinología'),  ('Endoscopía','Endoscopía'),
    ('Gastroenterología','Gastroenterología'),  ('Geriatría','Geriatría'),  ('Ginecología y obstetricia','Ginecología y obstetricia'),  ('Hematología','Hematología'),
    ('Infectología','Infectología'),  ('Laboratorio Clínico','Laboratorio Clínico'),  ('Medicina Física y Rehabilitación','Medicina Física y Rehabilitación'),  ('Medicina Interna','Medicina Interna'),
    ('Medicina Nuclear','Medicina Nuclear'),  ('Nefrología','Nefrología'),  ('Neonatalogía','Neonatalogía'),  ('Neumología','Neumología'),  ('Neurocirugia','Neurocirugia'),
    ('Neurofisiología Clínica','Neurofisiología Clínica'),  ('Neurología','Neurología'),  ('Oftalmologia','Oftalmologia'),  ('Oncología','Oncología'),  ('Ortopedia','Ortopedia'),
    ('Otorrinolaringología','Otorrinolaringología'),  ('Pediatría','Pediatría'),  ('Psiquiatría','Psiquiatría'),  ('Radiología e imagen','Radiología e imagen'),
    ('Reumatología','Reumatología'),('Salud Mental','Salud Mental'),  ('Trasplantes','Trasplantes'),  ('Unidad de Terapia Intensiva','Unidad de Terapia Intensiva'),
    ('Urgencias','Urgencias'),('Urología','Urología'),

     

]
class ContactForm(forms.ModelForm):

    class Meta:
        model = ModelValid
        fields = ['name','last_name','age','state_civil','n_hijos','lugar','profesion','especialidad','posgrado','time_ex','work','service','sick','who']
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name': forms.TextInput(attrs={'class':'form-control'})  ,
        'age' : forms.RadioSelect(choices=ages),
        'state_civil' : forms.RadioSelect(choices=estado_civil),
        'n_hijos' : forms.TextInput(attrs={'class':'form-control'}),
        'lugar' : forms.Select(choices=recidencia),
        'profesion' : forms.RadioSelect(choices=profes),
        'especialidad' : forms.RadioSelect(choices=yes_or_not),
        'posgrado' : forms.RadioSelect(choices=yes_or_not),
        'time_ex' : forms.Select(choices=experenciatime),
        'work' : forms.TextInput(attrs={'class':'form-control'}),
        'service' : forms.Select(choices=servicomedico),
        'sick' : forms.RadioSelect(choices=yes_or_not),
        'who' : forms.TextInput(attrs={'class':'form-control'}),
        }

    

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