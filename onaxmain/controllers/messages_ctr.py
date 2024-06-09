from django.http import JsonResponse, HttpRequest;
from django.urls import path;
from django.shortcuts import get_object_or_404;
from onaxmain.services.messages_service import MessagesService;
from common.helpers.logger_service import LoggerService as Logger;
from onaxmain.models.MessagesDto import MessagesDto;

logger = Logger();

def contact_options(request: HttpRequest):
    contact_svc = MessagesService().get_contact_options();
    return JsonResponse(contact_svc,safe=False, status=200 if contact_svc else 404);

def submit_contact(request: HttpRequest):
    if request.method == 'POST':
        contactObj: dict = request.body.decode('utf-8'); 
        isSaved = MessagesService().add_new_message(MessagesDto.from_json(contactObj));
        return JsonResponse({'message':'successful', 'isSuccessful': True}) if isSaved else JsonResponse({'message':'Message not sent.', 'isSuccessful': False});
    else:
        # Handle other HTTP methods (GET, PUT, DELETE, etc.) if necessary
        return JsonResponse({'error': 'Method not allowed'}, status=405)



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
    path("contact-options",contact_options, name="contact_options"),
    path("submit-contact",submit_contact, name="submit_contact")
]
#endregion