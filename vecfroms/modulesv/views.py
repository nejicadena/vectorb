from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
class ModulesPageView(CreateView):
    
    template_name= "modulesv/modulescar.html"
    
class ModulesPageView1(ListView):
    model = Comment
    template_name= "modulesv/module1.html" 

class CreateComment1(CreateView):
    model = Comment
    
    fields = ['content']
    template_name = "modulesv/createComment1.html"
    #success_url = reverse_lazy('modules1')

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.save()
        return redirect('modules1')

class ModulesPageView2(TemplateView):
    template_name= "modulesv/module2.html"     

class ModulesPageView3(TemplateView):
    template_name= "modulesv/module3.html"    
