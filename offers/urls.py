from django.urls import path
from offers import views

urlpatterns = [
    path('',views.AllOffersView.as_view(),name='all_offers'),
    path('food/',views.FoodOffersView.as_view(),name='food_offers'),
    path('drink/',views.DrinkOffersView.as_view(),name='drink_offers'),
    path('hukka/',views.DrinkOffersView.as_view(),name='hukka_offers'),
    path('beakery/',views.BeakeryOffersView.as_view(),name='beakery_offers'),


]

