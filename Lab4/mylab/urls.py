from django.urls import path
from . import views 


urlpatterns= [
    path("", views.default_views, name="default_views"),
    path("<int:amount>/", views.calculateTaxRate, name="calculateTaxRate"),
    path("taxRateView", views.taxRateView, name="taxRateView")

]