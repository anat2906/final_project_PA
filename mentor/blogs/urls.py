from django.conf.urls import url

from .views import TweetDetailView, TweetListView

urlpatterns = [
    url('', TweetListView.as_view(), name='list'),
    url('<int:pk>/', TweetDetailView.as_view(), name='detail'),
]
