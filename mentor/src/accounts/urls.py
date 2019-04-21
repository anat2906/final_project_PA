from django.urls import path, include
from django.views.generic import RedirectView

from accounts import views as user_views
from django.contrib.auth import views as auth_views
from accounts.views import UserRegisterView, UserBlog, UserFollower, UserView
# from blog.views import UserListView
from .views import (
    UserDetailView,
    UserFollowView,
)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('search/', UserView.as_view(), name='user_list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('<username>/', UserDetailView.as_view(), name='account_detail'),
    path('<username>/follow/', UserFollowView.as_view(), name='follow'),
    path('<username>/following/', UserFollower.as_view(), name='following'),# users whom i following
    path('<username>/blog/', UserBlog.as_view(), name='user_blog'),
]
