from django.db.models import QuerySet
from onaxmain.models.ContactOptions import ContactOptions
from onaxmain.models import MessagesDto;
from onaxmain.models.ContactOptions import ContactMessages;
from onaxmain.services.logger_service import LoggerService as Logger;

logger = Logger();

class MessagesService:
    '''Service class for Messages operations'''

    def get_contact_options(self)-> list[dict[ContactOptions]]:
        """Returns list[ContactOptionsDao] of all active or None"""
        try:
            objResult: QuerySet[ContactOptions] = ContactOptions.objects.filter(is_active=True).all();
            all_contacts = [{'key' : f"{item.id}",'value' : f"{item.option_name}"} for item in objResult]
        except Exception as e:
            print(f"Error in ContactOptionsDao.get_contact_options: {str(e)}");
            all_contacts = None;
        return all_contacts;

    def add_new_message(self, message_dto: MessagesDto)-> bool:
        """Adds a new message to the database"""
        try:
            print(message_dto);
            # Code here
            msg = ContactMessages(name=message_dto.name,
                    email=message_dto.email,
                    phone=message_dto.phone,
                    contact_option_id=message_dto.contact_option,
                    message=message_dto.message)
            msg.save();
            userId: int = msg.id;
            return userId > 0;            
        except Exception as e:
            print(f"Error in ContactOptionsDao.add_new_message: {str(e)}");
            logger.log(f"Error in MessagesService.add_new_message: {str(e)}");
            return False;
    