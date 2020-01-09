from django.urls import path
from . import views

name = 'users'

urlpatterns = [
    path('register/', views.register, name='users-register'),
]
