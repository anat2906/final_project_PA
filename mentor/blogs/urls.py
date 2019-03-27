from django.conf.urls import url

from .views import tweet_detail_view, tweet_list_view

urlpatterns = [
    url('', tweet_list_view, name='list'),
    url('', tweet_detail_view, name='detail'),
]
