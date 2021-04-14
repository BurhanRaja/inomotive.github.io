from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projecthome, name='projecthome'),
    path('<str:slug>', views.projectPost, name='projectPost'),
    path('projectsearch/', views.projectsearch, name='projectsearch'),
]