from django.shortcuts import render
from django.http import HttpResponse, HttpRequest;

# Create your views here.
def index(request: HttpRequest):
    # http://127.0.0.1:8000/home/?name=onadebi
    return HttpResponse(f"This site is currently under construction. {request.GET.get('name', 'No name provided')}")


def portfolio(request: HttpRequest):
    return HttpResponse("templates/portfolio.html", {'title': 'Portfolio'})
