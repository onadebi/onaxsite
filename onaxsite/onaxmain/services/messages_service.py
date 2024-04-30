from django.db.models import QuerySet
from onaxmain.models.ContactOptions import ContactOptions
from onaxmain.models import MessagesDto;
from onaxmain.services.logger_service import LoggerService as Logger;

logger = Logger();

class MessagesService:
    '''Service class for Messages operations'''

    def get_contact_options(self)-> list[dict[ContactOptions]]:
        """Returns list[ContactOptionsDao] of all active or None"""
        try:
            objResult: QuerySet[ContactOptions] = ContactOptions.objects.filter(is_active=True).all();
            all_contacts = [{item.id : f"{item.option_name}"} for item in objResult]
        except Exception as e:
            print(f"Error in ContactOptionsDao.get_contact_options: {str(e)}");
            all_contacts = None;
        return all_contacts;

    def add_new_message(self, message_dto: MessagesDto)-> bool:
        """Adds a new message to the database"""
        try:
            pass
        except Exception as e:
            print(f"Error in ContactOptionsDao.add_new_message: {str(e)}");
            logger.log(f"Error in MessagesService.add_new_message: {str(e)}");
            return False;
        return True;
    