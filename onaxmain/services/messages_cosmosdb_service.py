from azure.cosmos import exceptions
from onaxmain.services.logger_service import LoggerService as Logger;
from common.GenResponse import GenResponse;
from common.configs.dbConfig import DbConfig;
from typing import TypeVar,List

from onaxmain.models.MessagesDto import MessagesDto;

logger = Logger();

T = TypeVar('T', bound=MessagesDto)

class MessagesCosmosDbService:
    '''Service class for Messages operations on CosmosDB'''
    def __init__(self, db=None):
        self.dbCon = DbConfig(dbName=db, containerName='Messages');


    def get_items(self, query:str, params: dict)-> GenResponse[List[T]]:
        """Get items from the database using a query and parameters. Returns a GenResponse[List[T]] of items."""
        if not query:
            raise ValueError("The query parameter cannot be null or empty.")        
        #region Example of a parameterized query
        # parameterized_query = {
        #     'query': query,
        #     'parameters': params
        # }
        
        # return list(self.container.query_items(
        #     query=parameterized_query,
        #     enable_cross_partition_query=True
        # ))

        # Example usage
        # query = "SELECT * FROM c WHERE c.id = @id"
        # params = [{'name': '@id', 'value': 'some_id_value'}]
        # items = your_instance.get_items(query, params)
        #endregion       
        objResp = self.dbCon.getContainer().query_items(query=query, parameters=params, enable_cross_partition_query=True)
        return list(objResp);

    def add_messages(self, messages: list[MessagesDto]) -> bool:
        try:
            for message in messages:
                self.dbCon.getContainer().create_item(body=message.to_dict())
            return True
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error in DbConfig.add_messages: {str(e)}")
            return False