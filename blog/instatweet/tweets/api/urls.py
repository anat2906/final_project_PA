from django.urls import path
from django.views.generic import RedirectView

from .views import (
    TweetListAPIView,
)

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list'),
]
