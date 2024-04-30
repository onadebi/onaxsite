from django.http import JsonResponse, HttpRequest;
from django.urls import path;
from django.shortcuts import get_object_or_404;
from onaxmain.services.messages_service import MessagesService;
from onaxmain.services.logger_service import LoggerService as Logger;
from onaxmain.models.MessagesDto import MessagesDto;

logger = Logger();

def contact_options(request: HttpRequest):
    contact_svc = MessagesService().get_contact_options();
    return JsonResponse(contact_svc,safe=False, status=200 if contact_svc else 404);


def vote(request):
    submission = request.POST.get("contact_form", None);
    obj_result = {}; 
    bool_result = False;
    if submission == None:
        logger.log("No submission found in request");
        obj_result = {"error": "No submission found in request"};
    else:
        logger.log(f"Submission found in request: {submission}");
        message_dto = MessagesDto().from_json(submission);
        bool_result = MessagesService().add_new_message(message_dto);
    if bool_result:
        return JsonResponse(obj_result, status=200);
    else:
        return JsonResponse(obj_result, status=400);




#region Controller URL Patterns
contact_urlpatterns=[
    path("contact-options",contact_options, name="contact_options")
]
#endregion