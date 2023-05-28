from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


urlpatterns = [
    path('register/',views.CreateUser.as_view(),name='create_user'),
    path('login/',views.LoginView.as_view(),name='user_login'),
]
