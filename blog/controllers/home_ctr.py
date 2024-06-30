from django.shortcuts import render;
from django.urls import path;
from django.http import HttpRequest, HttpResponse;
from blog.services.PostService import PostService;
from common.helpers.logger_service import LoggerService as Logger;

logger = Logger();

def index(request: HttpRequest):
    posts = PostService().get_all();
    context: dict={'title': 'Blog',
                   'description': 'Onaxsys Media Blog',
                   "posts": posts,
                   "featured_post": PostService().get_featured_post()};
    logger.log(message=context)
    return render(request, "blog/index.html", context);



#region Controller Urls
blog_urlpatterns = [
    path("", index, name="index")
]
#endregion
