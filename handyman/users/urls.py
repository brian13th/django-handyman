from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

name = 'users'

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('profile/', views.profile, name='users-profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
]
