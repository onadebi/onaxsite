from django.shortcuts import render
from django.http import HttpResponse, HttpRequest;

# Create your views here.
def index(request: HttpRequest):
    # http://127.0.0.1:8000/home/?name=onadebi
    return HttpResponse(f"Hello, world. You're at the polls index. {request.GET.get('name', 'No name provided')}")
