from django.urls import path
from .views import UserSignup, UserSignin, UserList

urlpatterns = [
    path("signup/", UserSignup.as_view()),
    path("signin/", UserSignin.as_view()),
    path("users/", UserList.as_view()),
]