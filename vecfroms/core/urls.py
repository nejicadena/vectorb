from django.urls import path
from .views import HomePageView, SamplePageView, AboutPageView, AcercaTallerPageView, AquienPageView, QuienimpartePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('enqueconsiste/', AcercaTallerPageView.as_view(), name="enqueconsiste"),
    path('aquiensedirige/', AquienPageView.as_view(), name="aquiensedirige"),
    path('quienimparte/', QuienimpartePageView.as_view(), name="quienimparte"),
]