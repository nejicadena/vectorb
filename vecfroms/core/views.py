from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

class AboutPageView(TemplateView):
    template_name = "core/about.html"
    
class SamplePageView(TemplateView):
    template_name = "core/sample.html"

class AcercaTallerPageView(TemplateView):
    template_name = "core/enqueconsiste.html"  

class AquienPageView(TemplateView):
    template_name = "core/aquiensedirige.html"

class QuienimpartePageView(TemplateView):
    template_name = "core/quienimparte.html"