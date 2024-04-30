from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpRequest, JsonResponse;

# Create your views here.
def index(request: HttpRequest):
    # http://127.0.0.1:8000/home/?name=onadebi
    # return HttpResponse(f"This site is currently under construction. {request.GET.get('name', 'No name provided')}")
    context: dict = {
        'description': 'Trust us to bring your digital expectations to life.',};
    return render(request, "onaxmain/index.html",context)

def about(request: HttpRequest):
    context: dict={'title': 'About Onaxsys Media',
                   'description': 'Get to know us.'};
    return render(request, "onaxmain/about.html", context)

def portfolio(request: HttpRequest):
    return render(request,"onaxmain/portfolio.html", {'title': 'Portfolio'})

def contact(request: HttpRequest):
    context: dict=  {'title': 'Get in touch with us'};
    return render(request, "onaxmain/contact.html",context)

