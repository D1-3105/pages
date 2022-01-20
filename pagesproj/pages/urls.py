from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path("about", AboutView.as_view(), name='about'),
]