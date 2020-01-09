from django.urls import path
from .views import (
    PostListView,
    PostDetailView
    )

name = 'main'

urlpatterns = [
    path('', PostListView.as_view(), name='main-view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='main-detail'),
]
