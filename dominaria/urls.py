from django.urls import path
from . import views

urlpatterns = [
    path('', views.classif, name='dominaria-classif'),
    path('partides/', views.games, name='dominaria-home'),
]