from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit/<str:title>", view=views.edit, name="edit"),
    path("random", view=views.random, name="random"),
]
