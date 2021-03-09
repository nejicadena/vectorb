from django.urls import path
from .views import newModulesPageView,newModulesPageView1, newModulesPageView11,newModulesPageView12,newModulesPageView13,newModulesPageView14

urlpatterns = [
    path('', newModulesPageView.as_view(), name="newmodulemain"),
    path('newmodule1/', newModulesPageView1.as_view(), name="newmodule1"),
    path('newmodule11/', newModulesPageView11.as_view(), name="newmodule11"),
    path('newmodule12/', newModulesPageView12.as_view(), name="newmodule12"),
    path('newmodule13/', newModulesPageView13.as_view(), name="newmodule13"),
    path('newmodule14/', newModulesPageView14.as_view(), name="newmodule14"),

    
]