from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from django.shortcuts import render, get_list_or_404
from django.views.generic import (
                CreateView,
                DetailView,
                DeleteView,
                ListView,
                UpdateView
                )

from .mixins import FormUserNeededMixin
from .models import Tweet
from .forms import TweetModelForm


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/blog/create/"
    # login_url = "/admin/"


class TweetUpdateView(UpdateView):
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    success_url = "/tweet/"


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(LoginRequiredMixin, ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context

