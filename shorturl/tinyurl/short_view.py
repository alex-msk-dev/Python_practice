from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render
from .full_url_form import FullUrlFrom

# Create your views here.

def short_url(request: HttpRequest):
    if request.method !='POST':
        return HttpResponseNotAllowed(['POST'])
    url_form = FullUrlForm(request.POST)
    if not url_form.is_valid():
        return HttpResponseBadRequest()
    url = url_form.cleaned_data['url']
    return render(request, 'short.html', {'url': url})