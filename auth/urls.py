from django.urls import path
from auth import views

urlpatterns = [

    path("signup/", views.Signup, name="signup"),
    path("login/", views.Login, name="login"),
    path("reset/", views.Reset, name="reset")
]