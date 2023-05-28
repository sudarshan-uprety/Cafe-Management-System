from django.urls import path

from foods import views

urlpatterns = [
    path('',views.AllFoods.as_view(),name='foods'),
    path('veg/',views.vegFoods.as_view(),name='veg'),
    path('nonveg/',views.NonVegFood.as_view(),name='non_veg'),

]
