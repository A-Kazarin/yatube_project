from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<int:pk>/', views.ice_cream_detail),
    path('group/<slug:slug>/',views.group_posts)
]