from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('login', views.login_spotify, name='login_spotify'),
    path('events', views.display_events, name='display_events'),
]