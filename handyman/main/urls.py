from django.urls import path
from . import views
name = 'main'

urlpatterns = [
    path('', views.base, name='base'),
]
