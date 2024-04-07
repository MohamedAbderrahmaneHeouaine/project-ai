from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.goForm, name='goForm'),
    path('submit/', views.submit_form, name='submit_form'),
    path('counter/', views.counter, name='counter')
]
