from django.urls import path

from category import views

urlpatterns = [
    path('foods/',views.FoodCategoryView.as_view(),name='foods_category'),
    path('drinks/',views.DrinkCategoryView.as_view(),name='drinks_category'),
    path('hukka/',views.HukkaCategoryView.as_view(),name='hukka_category'),
    path('beakery/',views.BeakeryCategoryView.as_view(),name='beakery_category'),

]
