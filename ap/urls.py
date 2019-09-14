from django.urls import path, include
from django.conf.urls import url
from .views import index, email, signup

urlpatterns = [
    path("", index, name="index"),
    path("login", email, name='login'),
    path("signup", signup, name="signup"),
]
