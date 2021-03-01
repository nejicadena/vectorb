from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class newModulesPageView(TemplateView):
    
    template_name= "newmodules/newmodulemain.html"
    
    
class newModulesPageView1(TemplateView):
    
    template_name= "newmodules/newmodule1.html" 
    
class newModulesPageView11(TemplateView):
   
    template_name= "newmodules/newmodule11.html" 
    
class newModulesPageView12(TemplateView):

    template_name= "newmodules/newmodule12.html" 