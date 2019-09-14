from django.urls import path, include
from django.conf.urls import url
from .views import index, login, signup

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name='login'),
    path("signup", signup, name="signup"),
]
