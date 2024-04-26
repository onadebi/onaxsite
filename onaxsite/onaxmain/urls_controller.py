from django.urls import path;
from . import views;

app_name = "onaxmain";
urlpatterns = [
    path("",views.index, name="index"),
    path("portfolio",views.portfolio, name="portfolioz"),
    path("about",views.about, name="about"),
]