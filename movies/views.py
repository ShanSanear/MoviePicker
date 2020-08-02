from django.shortcuts import render


# Create your views here.

def movies_search_view(request, *args, **kwargs):
    return render(request, 'movies_search.html', context={})


def movies_rate_view(request, *args, **kwargs):
    return render(request, 'movies_rate.html', context={})


def movies_watch_view(request, *args, **kwargs):
    return render(request, 'movies_watch.html', context={})
