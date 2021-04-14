from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # APIs to post comment
    path('postComment', views.postComment, name="postComment"),

    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    path('search/', views.search, name='search'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)