from django.urls import path
from django.views.generic import TemplateView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )

name = 'main'

urlpatterns = [
    path('', PostListView.as_view(), name='main-view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='main-detail'),
    path('post/create/', PostCreateView.as_view(), name='main-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='main-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='main-delete'),
    path('contact/', TemplateView.as_view(template_name='main/contact.html'), name='main-contact'),
]
