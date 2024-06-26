from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nico", views.nico, name="nico"),
    path("<str:name>", views.greet, name="greet")
]