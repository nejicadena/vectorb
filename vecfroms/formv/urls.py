from django.urls import path
from .views import ContactView, BornoutView

urlpatterns = [
    path('',ContactView.as_view(), name="form"),
    path('bornout/', BornoutView, name="formBornout")
    
]