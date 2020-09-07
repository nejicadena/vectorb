from django.urls import path
from .views import ContactView, BornoutView, ConsentiView

urlpatterns = [
    path('',ConsentiView.as_view(), name="form"),
    path('contact/',ContactView.as_view(), name="formcontact"),
    path('bornout/', BornoutView, name="formBornout")
    
]