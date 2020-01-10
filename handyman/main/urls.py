from django.urls import path
from django.views.generic import TemplateView
from .views import (
    PostListView,
    PostDetailView
    )

name = 'main'

urlpatterns = [
    path('', PostListView.as_view(), name='main-view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='main-detail'),
    path('contact/', TemplateView.as_view(template_name='main/contact.html'), name='main-contact'),
]
