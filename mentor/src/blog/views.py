from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.forms import inlineformset_factory
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
                CreateView,
                DetailView,
                DeleteView,
                ListView,
                UpdateView
                )

from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Blog, BlogImage
from .forms import *


def create_post(request):
    form = BlogForm(request.POST or None)
    BlogImageFormSet = inlineformset_factory(Blog, BlogImage, form=BlogImageForm, extra=1, can_delete=True)
    if request.method == 'POST':
        if form.is_valid():

            user = request.user
            form.instance.user = user
            blog = form.save()
            formset = BlogImageFormSet(request.POST, request.FILES, instance=blog)
            if formset.is_valid():
                formset.save()
            return redirect(blog.get_absolute_url())
    formset = BlogImageFormSet()
    return render(request, 'blog/create_view.html', locals())


@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=blog)
    title = 'Update a blog'
    BlogImageFormSet = inlineformset_factory(Blog, BlogImage, form=BlogImageForm, extra=0, can_delete=True)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save()
            formset = BlogImageFormSet(request.POST, request.FILES, instance=blog)
            if formset.is_valid():
                formset.save()
            return redirect(product.get_absolute_url())
    formset = BlogImageFormSet(instance=blog)
    return render(request, 'blog/update_view.html', locals())


class BlogDeleteView(UserOwnerMixin, UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/delete_confirm.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.user:
            return True
        return False


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(BlogListView, self).get_queryset(**kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            ).order_by("-timestamp")
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        return context


class UserBlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "blog/user_blog_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Blog.objects.all()
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


class UserListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "accounts/user_list_view.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(UserListView, self).get_queryset(**kwargs)
        qs = qs.filter(user=self.user).order_by("-timestamp")
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).order_by("-timestamp")
        return qs

