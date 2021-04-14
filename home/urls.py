from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contactme', views.contactme, name='contactme'),
    path('signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)