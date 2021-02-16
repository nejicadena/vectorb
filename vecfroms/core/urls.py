from django.urls import path
from .views import HomePageView, SamplePageView, AboutPageView, AcercaTallerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('acerca/', AcercaTallerPageView.as_view(), name="acerca"),
]