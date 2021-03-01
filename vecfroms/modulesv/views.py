from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Comment, Comment2, Comment3
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
class ModulesPageView(TemplateView):
    
    template_name= "modulesv/modulesmain.html"
    
class ModulesPageView1(TemplateView):
    
    template_name= "modulesv/module1.html" 
class ModulesPageView11(TemplateView):
   
    template_name= "modulesv/module11.html" 
class ModulesPageView12(TemplateView):

    template_name= "modulesv/module12.html"       

# class CreateComment1(CreateView):
#     model = Comment
    
#     fields = ['content1']
    
#     template_name = "modulesv/createComment1.html"
#     #success_url = reverse_lazy('modules1')

#     def form_valid(self,form):
#         contentUs = self.request.POST.get('content1')
#         print(contentUs)
#         all_entries = Comment.objects.all()
#         form.instance.user = self.request.user
#         form.save()
#         return redirect('modules1')

# class ModulesPageView2(ListView):
#     model = Comment2
#     template_name= "modulesv/module2.html"

# class CreateComment2(CreateView):
#     model = Comment2
    
#     fields = ['content2']
#     template_name = "modulesv/createComment2.html"
#     #success_url = reverse_lazy('modules1')

#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         form.save()
#         return redirect('modules2')

# class ModulesPageView3(ListView):
#     model = Comment3
#     template_name= "modulesv/module3.html" 

# class CreateComment3(CreateView):
#     model = Comment3
    
#     fields = ['content3']
#     template_name = "modulesv/createComment3.html"
#     #success_url = reverse_lazy('modules1')

#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         form.save()
#         return redirect('modules3')

# class LayerModel1(ListView):
#     template_name = "modulesv/layer1.html"

# class LayerModel2(ListView):
#     template_name = "modulesv/layer2.html"

# class LayerModel3(ListView):
#     template_name = "modulesv/layer3.html"

