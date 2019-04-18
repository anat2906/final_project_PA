from django.urls import path
from django.views.generic import RedirectView

from .views import (
    BlogListAPIView,
    BlogCreateAPIView,
)

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='list'),
    path('create/', BlogCreateAPIView.as_view(), name='create'),
]