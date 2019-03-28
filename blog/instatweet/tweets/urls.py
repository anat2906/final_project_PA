from django.conf.urls import url

from .views import (
    TweetCreateView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView
)

urlpatterns = [
    url('create/', TweetCreateView.as_view(), name='create'),
    url('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    url('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    url('', TweetListView.as_view(), name='list'),
]
