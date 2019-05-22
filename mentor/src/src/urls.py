"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


from blog.views import BlogListView
from accounts.views import user_list
from .views import SearchView, about_page, faq, agreement
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('total/', BlogListView.as_view(), name='total'),#общий блог
    path('about/', about_page, name="about"),
    path('faq/', faq, name="faq"),
    path('agreement/', agreement, name="agreement"),
    path('', user_list, name='home'),
    # path('user/search/', SearchView.as_view(), name='search'),#all mentor list
    path('', include(('accounts.urls', 'profiles'), namespace='profiles')),
    path('api/blog/', include(('blog.api.urls', 'blog-api'), namespace='blog-api')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('', include('django.contrib.auth.urls')),
    path('403', views.forbidden_view, name='403')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
