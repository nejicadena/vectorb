from django.urls import path
from .views import newModulesPageView,newModulesPageView1, newModulesPageView11,newModulesPageView12

urlpatterns = [
    path('', newModulesPageView.as_view(), name="newmodulemain"),
    path('newmodule1/', newModulesPageView1.as_view(), name="newmodule1"),
    path('newmodule11/', newModulesPageView11.as_view(), name="newmodule11"),
    path('newmodule12/', newModulesPageView12.as_view(), name="newmodule12"),

    
]