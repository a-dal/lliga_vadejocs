from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dominaria-home'),
    path('classificacio/', views.about, name='dominaria-classif'),
]