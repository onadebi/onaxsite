from django.db.models import QuerySet
from onaxmain.models.ContactOptions import ContactOptions
from onaxmain.models import MessagesDto;
from onaxmain.models.ContactOptions import ContactMessages;
from common.helpers.logger_service import LoggerService as Logger
from onaxmain.services.messages_cosmosdb_service import MessagesCosmosDbService;

logger = Logger();

class MessagesService:
    '''Service class for Messages operations'''

    def get_contact_options(self)-> list[dict[ContactOptions]]:
        """Returns list[ContactOptionsDao] of all active or None"""
        try:
            objResult: QuerySet[ContactOptions] = ContactOptions.objects.filter(is_active=True).all();
            all_contacts = [{'key' : f"{item.id}",'value' : f"{item.option_name}"} for item in objResult]
        except Exception as e:
            logger.log(f"Error in ContactOptionsDao.get_contact_options: {str(e)}");
            all_contacts = None;
        return all_contacts;

    def add_new_message(self, message_dto: MessagesDto)-> bool:
        """Adds a new message to the database"""
        try:
            logger.log(message_dto);
            # Code here
            msg = ContactMessages(name=message_dto.name,
                    email=message_dto.email,
                    phone=message_dto.phone,
                    contact_option_id=message_dto.contact_option,
                    message=message_dto.message)
            msg.save();
            userId: int = msg.id;
            try:
                logger.log(f"===Saving message of userId: {userId} to cosmosdb===");
                messsage_service = MessagesCosmosDbService();
                result = messsage_service.add_messages([message_dto], userId);
                if result:
                    logger.log(f"===Message of userId: {userId} saved to cosmosdb===");
                else:
                    logger.log(f"===Error saving message of userId: {userId} to cosmosdb===");       
            except Exception as e:
                logger.log(f"Error in MessagesService.add_new_message: {str(e)}");
            return userId > 0;            
        except Exception as e:
            logger.log(f"Error in ContactOptionsDao.add_new_message: {str(e)}");
            logger.log(f"Error in MessagesService.add_new_message: {str(e)}");
            return False;
    