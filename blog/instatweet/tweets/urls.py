from django.urls import path

from .views import (
    TweetCreateView,
    TweetDetailView,
    TweetDeleteView,
    TweetListView,
    TweetUpdateView
)

urlpatterns = [
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', TweetUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),

]
