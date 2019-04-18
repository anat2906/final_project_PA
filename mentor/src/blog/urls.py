from django.urls import path
from django.views.generic import RedirectView

from .views import (
    create_post,
    BlogDetailView,
    BlogDeleteView,
    BlogListView,
    # BlogUpdateView
    update_blog,
    UserBlogListView,
)

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('search/', BlogListView.as_view(), name='list'),
    path('list/', UserBlogListView.as_view(), name='user_blog_list'),
    path('create/', create_post, name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:id>/edit/', update_blog, name='edit'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),

]