from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from blog.models import Blog

from .pagination import StandardResultsPagination
from .serializers import BlogModelSerializer


class BlogCreateAPIView(generics.CreateAPIView):
    serializer_class = BlogModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogListAPIView(generics.ListAPIView):
    serializer_class = BlogModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        me_following = self.request.user.profile.get_following()
        qs1 = Blog.objects.filter(user__in=me_following)
        qs2 = Blog.objects.filter(user=self.request.user)
        qs = (qs1 | qs2).distinct().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs
