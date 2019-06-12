from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, FormView, ListView

from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import User
from .models import UserProfile



class UserRegisterView(FormView):
    template_name = 'accounts/user_register_form.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        user_type = form.cleaned_data.get("user_type")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(
            username=username,
            email=email,
            user_type=user_type,
            first_name=first_name,
            last_name=last_name
        )
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)


class UserDetailView(DetailView):
    template_name = "accounts/user_detail.html"
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context["following"] = UserProfile.objects.is_following(self.request.user, self.get_object())
            context['recommended'] = UserProfile.objects.recommended(self.request.user)
            return context
        return context


class UserFollower(DetailView):
    template_name = "accounts/following.html"
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, *args, **kwargs):
        context = super(UserFollower, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context["following"] = UserProfile.objects.is_following(self.request.user, self.get_object())
            context['recommended'] = UserProfile.objects.recommended(self.request.user)
            return context
        return context


class UserBlog(DetailView):
    template_name = "accounts/blog_user_list.html"
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))


class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated:
            is_following = UserProfile.objects.toogle_follow(request.user, toggle_user)
        return redirect("profiles:account_detail", username=username)


class UserView(ListView):
    model = User
    template_name = "search.html"

    def get_queryset(self):
        return User.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super(UserView, self).get_queryset(**kwargs).exclude(user_type="Student")
        # qs = User.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(username__icontains=query) |
                Q(profile__position__icontains=query)
            )
        return qs


def user_list(request):
    users = User.objects.all().exclude(user_type="Student").order_by('?')[:3]
    return render(request, 'home.html', locals())


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profiles:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)
