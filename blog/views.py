from django.shortcuts import render
from django.http import HttpRequest
from common.helpers.logger_service import LoggerService;

logger = LoggerService();

# Create your views here.
def index(request: HttpRequest):
    context: dict={'title': 'About Onaxsys Media',
                   'description': 'Get to know us.'};
    logger.log(message=context)
    return render(request, "blog/index.html", context);