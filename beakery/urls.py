from django.urls import path
from beakery import views

urlpatterns = [
    path('',views.AllBeakeryProduct.as_view(),name='beakery'),
]
