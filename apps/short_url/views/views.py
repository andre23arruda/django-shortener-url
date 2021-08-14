from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext

from short_url.models import Url


def redirect_url(request, short_url):
    '''Redirect short url to long url'''
    url = get_object_or_404(Url, short_url=short_url)
    if url.is_valid():
        return redirect(url.long_url)
    raise Http404('Desculpe, este link está inválido :(')


def error_404_view(request, exception):
    return render(request,'error/404.html')

def error_500_view(request, exception=None):
    return render(request,'error/500.html')