from django.urls import path

from hukka import views

urlpatterns = [
    path('',views.HukkaView.as_view(),name='hukkas'),
]

