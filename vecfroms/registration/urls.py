from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, ConsentPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('consenti/', ConsentPageView.as_view(), name="consentimiento"),
    
]