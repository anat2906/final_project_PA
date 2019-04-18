from django.urls import path, include
from django.views.generic import RedirectView

from accounts import views as user_views
from accounts.views import UserRegisterView
from .views import (
    UserDetailView,
    UserFollowView,
)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('<username>/', UserDetailView.as_view(), name='account_detail'),
    path('<username>/follow/', UserFollowView.as_view(), name='follow'),

]
