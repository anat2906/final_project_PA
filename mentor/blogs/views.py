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


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "blogs/create_view.html"
    success_url = "/blog/create/"
    login_url = "/admin/"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(TweetCreateView, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
            return self.form_invalid(form)


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


