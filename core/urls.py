from django.urls import path
from .views import *

urlpatterns = [
    path('',homePage,name="home"),
    path('register',signUpView,name="register"),
    path('login',signIn,name="login"),
    path('logout',signoutView,name="logout"),
]