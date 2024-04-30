from django.urls import path, include;
from . import views;
import onaxmain.controllers.messages_ctr as messages_ctr;

app_name = "onaxmain";
urlpatterns = [
    path("",views.index, name="index"),
    path("portfolio",views.portfolio, name="portfolioz"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),

    # APIs and Controllers
    path("",include(messages_ctr.contact_urlpatterns))
]