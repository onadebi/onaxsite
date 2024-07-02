from django.urls import path, include;
import blog.controllers.home_ctr as home_ctr;

app_name="posts"
urlpatterns=[
    # path("", views.index, name="index"),
    path("", include(home_ctr.blog_urlpatterns))

]