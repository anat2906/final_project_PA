from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from blog.models import Blog


def is_anonymous(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def is_mentor_manager(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not request.user.user_type == 'Mentor':
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def can_create_blog(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not request.user.user_type == 'Mentor':
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def can_update_blog(func):
    def wrapper(request, pk, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        product = get_object_or_404(Product, pk=pk)
        if not user.user_type == 'Mentor':
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, pk, *args, **kwargs)
    return wrapper


def can_delete_blog(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not request.user.user_type == 'Mentor':
            if request.is_ajax():
                return JsonResponse({
                    'error': True,
                    'errors': ['You don\'t have permission to perfom the process!'],
                    'redirect_url': settings.FORBIDDEN_REDIRECT_URL
                })
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper
