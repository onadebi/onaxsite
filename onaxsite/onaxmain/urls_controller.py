from django.urls import path, include;
from . import views;
import onaxmain.controllers.messages_ctr as messages_ctr;
from onaxsite.settings import DEBUG;

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contactoptions', views.ContactOptionsViewSet)

app_name = "onaxmain";
urlpatterns = [
    path("",views.index, name="index"),
    path("portfolio",views.portfolio, name="portfolioz"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path('swagger', include(router.urls)),

    # APIs and Controllers
    path("api/messages/",include(messages_ctr.contact_urlpatterns))
];
if DEBUG:
    urlpatterns.append(path('api-auth/',include('rest_framework.urls', namespace='rest_framework')))