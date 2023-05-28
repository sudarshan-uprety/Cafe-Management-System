from django.urls import path

from drinks import views

urlpatterns = [
    path('',views.AllDrinks.as_view(),name='drinks'),
    path('alcohol/',views.AlcoholDrinks.as_view(),name='alcohols'),
    path('nonalcohol/',views.NonAlcoholDrinks.as_view(),name='nonalcohols'),

]
