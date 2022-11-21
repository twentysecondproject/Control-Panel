from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('persona/<int:persons_id>', views.instance),
    path('delete/<int:persons_id>', views.delete),
]
