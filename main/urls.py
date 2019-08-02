from django.urls import path
from main import views


urlpatterns = [


    path('', views.Index, name="index"),
    path("article/<int:pk>", views.Article, name="article"),
    path("auth/signup", views.Signup, name="signup"),
    path("auth/login", views.Login, name="login")

]