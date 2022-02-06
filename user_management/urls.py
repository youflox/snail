from django.urls import path

from .viewset import UserLoginView, UserSignupView, UserLogoutView


urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('signup/', UserSignupView.as_view()),
    path('logout/', UserLogoutView.as_view()),

]
