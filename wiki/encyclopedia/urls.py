from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.title, name="title"),
    path("createpage", views.createpage, name="createpage"),
    path("wiki/edit/<title>", views.edit, name="edit"),
    path("search", views.search, name="search")
]
