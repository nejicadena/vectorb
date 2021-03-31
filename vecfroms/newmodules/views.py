from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import Module12Form

# Create your views here.

class newModulesPageView(TemplateView):
    
    template_name= "newmodules/newmodulemain.html"
    
    
class newModulesPageView1(TemplateView):
    
    template_name= "newmodules/newmodule1.html" 
    
class newModulesPageView11(TemplateView):
   
    template_name= "newmodules/newmodule11.html" 
    
class newModulesPageView12(FormView):

    template_name= "newmodules/newmodule12.html" 
    form_class = Module12Form
    success_url = 'newmodule13'
    def form_valid(self,form):
        form.instance.user = self.request.user
        form.save()
        return redirect('newmodule13')

class newModulesPageView13(TemplateView):

    template_name= "newmodules/newmodule13.html" 

class newModulesPageView14(TemplateView):

    template_name= "newmodules/newmodule14.html" 