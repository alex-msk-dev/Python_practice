from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .full_url_form import  FullUrlFrom
# Create your views here.

def index(request: HttpRequest):
    full_url_form = FullUrlFrom()
    return render(request, 'dr.html',{'url_form': full_url_form})
