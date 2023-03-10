from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("wiki/<str:title>/", views.inpage, name="inpage"),
    path("search/", views.search, name="search"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random/", views.random, name="random"),
]

