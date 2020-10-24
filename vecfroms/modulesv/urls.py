from django.urls import path
from .views import ModulesPageView, ModulesPageView1, ModulesPageView2, ModulesPageView3, CreateComment1,CreateComment2, CreateComment3 ,LayerModel1,LayerModel2,LayerModel3

urlpatterns = [
    path('', ModulesPageView.as_view(), name="modules"),
    path('1', ModulesPageView1.as_view(), name="modules1"),
    path('2', ModulesPageView2.as_view(), name="modules2"),
    path('3', ModulesPageView3.as_view(), name="modules3"),
    path('comentario', CreateComment1.as_view(), name="comment1"),
    path('comentario2', CreateComment2.as_view(), name="comment2"),
    path('comentario3', CreateComment3.as_view(), name="comment3"),
    path('1/layer1', LayerModel1.as_view(),name="layer1"),
    path('2/layer2', LayerModel2.as_view(),name="layer2"),
    path('3/layer3', LayerModel3.as_view(),name="layer3"),
    
]