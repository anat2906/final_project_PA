from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
                CreateView,
                DetailView,
                DeleteView,
                ListView,
                UpdateView
                )

from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet
from .forms import TweetModelForm


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"


class TweetUpdateView(UserOwnerMixin, LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list")


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                           )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context
