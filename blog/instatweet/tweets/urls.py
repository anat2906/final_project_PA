from django.urls import path
from django.views.generic import RedirectView

from .views import (
    TweetCreateView,
    TweetDetailView,
    TweetDeleteView,
    TweetListView,
    TweetUpdateView
)

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('search/', TweetListView.as_view(), name='search'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', TweetUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),

]
