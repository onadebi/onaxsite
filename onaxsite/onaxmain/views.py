from django.shortcuts import render
from django.http import HttpResponse, HttpRequest;

# Create your views here.
def index(request: HttpRequest):
    # http://127.0.0.1:8000/home/?name=onadebi
    # return HttpResponse(f"This site is currently under construction. {request.GET.get('name', 'No name provided')}")
    context: dict = {
        'description': 'Trust us to bring your digital expectations to life.',
        'title': 'Onaxsys Media',
    };
    return render(request, "onaxmain/index.html",context)

def about(request: HttpRequest):
    return render(request, "onaxmain/about.html", {'title': 'Onadebi\'s About Page'})

def portfolio(request: HttpRequest):
    return render(request,"onaxmain/portfolio.html", {'title': 'Portfolio'})
