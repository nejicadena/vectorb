from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class ModulesPageView(TemplateView):
    template_name= "modulesv/modulescar.html"

class ModulesPageView1(TemplateView):
    template_name= "modulesv/module1.html" 

class ModulesPageView2(TemplateView):
    template_name= "modulesv/module2.html"     

class ModulesPageView3(TemplateView):
    template_name= "modulesv/module3.html"    
