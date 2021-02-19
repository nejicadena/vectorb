from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, ConsentPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('consen/', ConsentPageView.as_view(), name="consenti"),
    
]