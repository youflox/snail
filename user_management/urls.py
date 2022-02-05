from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import home, login, signup, logout
from .viewset import UserLoginView, UserSignupView, UserLogoutView


urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('signup/', UserSignupView.as_view()),
    path('logout/', UserLogoutView.as_view()),

]
