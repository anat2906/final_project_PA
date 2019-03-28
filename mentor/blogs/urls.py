from django.conf.urls import url

from .views import (
    TweetCreateView,
    TweetDetailView,
    TweetListView,
)

urlpatterns = [
    url('blog/create/', TweetCreateView.as_view(), name='create'),
    url('blog/<int:pk>/', TweetDetailView.as_view(), name='detail'),
    url('', TweetListView.as_view(), name='list'),
]
