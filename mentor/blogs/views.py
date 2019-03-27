from django.shortcuts import render


def tweet_detail_view(request):
    return render(request, "blogs/detail_view.html", {})


def tweet_list_view(request):
    return render(request, "blogs/list_view.html", {})
