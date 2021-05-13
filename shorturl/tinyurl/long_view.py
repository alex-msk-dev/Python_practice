from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from .storage import shorts

# Create your views here.

def full_url(request: HttpRequest, key):
    try:
        url = shorts[key]
        if url.startswith('http'):
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(f'http://{url}')
    except KeyError:
        return HttpResponseNotFound()
