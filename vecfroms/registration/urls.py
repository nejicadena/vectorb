from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, ConsentPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('consen/', TemplateView.as_view(template_name='registration/consentimiento.html'), name="con"),
    
]