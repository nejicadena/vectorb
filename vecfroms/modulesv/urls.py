from django.urls import path
from .views import ModulesPageView, ModulesPageView1, ModulesPageView2, ModulesPageView3

urlpatterns = [
    path('', ModulesPageView.as_view(), name="modules"),
    path('1', ModulesPageView1.as_view(), name="modules1"),
    path('2', ModulesPageView2.as_view(), name="modules2"),
    path('3', ModulesPageView3.as_view(), name="modules3"),
    
]