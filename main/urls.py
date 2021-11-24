from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main ,name = 'main' ),
    path('upload/<str:pk>', views.upload, name = 'upload'),
]