from django.shortcuts import render;
from django.urls import path;
from django.http import HttpRequest, HttpResponse;
from blog.models.Posts import Posts
from blog.services.PostService import PostService;
from common.helpers.logger_service import LoggerService as Logger;

logger = Logger();

def index(request: HttpRequest):
    posts = PostService().get_all();
    context: dict={'title': 'Blog',
                   'description': 'Blog Posts',
                   "posts": posts,
                   "featured_post": PostService().get_featured_post()};
    logger.log(message=context)
    return render(request, "blog/index.html", context);


def post_detail(request: HttpRequest, slug: str):
    detail_post: Posts = PostService().get_by_id(slug);
    title: str = detail_post['post_title'] if detail_post is not None else 'Blog';
    context: dict={'title': title,
                   'description': detail_post['post_summary'] if detail_post is not None else 'Onaxsys Media Blog',
                   'keywords': f'{title}',
                   "post": detail_post};
    logger.log(message=context)
    return render(request, "blog/post-detail.html", context);



#region Controller Urls
blog_urlpatterns = [
    path("", index, name="index"),
    path("<slug:slug>/", post_detail, name="post_detail"),
]
#endregion
