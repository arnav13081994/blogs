from django.urls import path
from main import views


urlpatterns = [


    path('', views.Index, name="index"),
    path("article/<int:pk>", views.Article, name="article"),

]