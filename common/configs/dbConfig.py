from azure.cosmos import CosmosClient,exceptions, PartitionKey, ContainerProxy;
from decouple import config;

import json;
import asyncio

from common import GenResponse
from onaxmain.models.MessagesDto import MessagesDto;

COSMOS_DB_ENDPOINT = config('COSMOS_DB_ENDPOINT', cast=str)
COSMOS_DB_KEY = config('COSMOS_DB_KEY', cast=str)
COSMOS_DB_NAME = config('COSMOS_DB_NAME', cast=str)
COSMOS_CONTAINER_NAME = config('COSMOS_CONTAINER_NAME', cast=str)

client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY)

db: CosmosClient = client.get_database_client(COSMOS_DB_NAME)
container: ContainerProxy = db.get_container_client(COSMOS_CONTAINER_NAME)

class DbConfig:
    def __init__(self, dbName=None, containerName=None):
        if dbName is None:
            self.db = client.get_database_client(COSMOS_DB_NAME)
        else:
            self.db = client.get_database_client(dbName)
        if containerName is None:
            self.container = self.db.get_container_client(COSMOS_CONTAINER_NAME)
        else:
            self.container = self.db.get_container_client(containerName.lower())

    def getContainer(self) -> ContainerProxy:
        """Returns the container object, which is of type :ContainerProxy, from azure.cosmos package"""
        return self.container;



    # def get_items(self, query:str, params: dict)-> GenResponse[List[T]]:
    #     """Get items from the database using a query and parameters. Returns a GenResponse[List[T]] of items."""
    #     if not query:
    #         raise ValueError("The query parameter cannot be null or empty.")        
    #     #region Example of a parameterized query
    #     # parameterized_query = {
    #     #     'query': query,
    #     #     'parameters': params
    #     # }
        
    #     # return list(self.container.query_items(
    #     #     query=parameterized_query,
    #     #     enable_cross_partition_query=True
    #     # ))

    #     # Example usage
    #     # query = "SELECT * FROM c WHERE c.id = @id"
    #     # params = [{'name': '@id', 'value': 'some_id_value'}]
    #     # items = your_instance.get_items(query, params)
    #     #endregion       
    #     objResp =  self.container.query_items(query=query, parameters=params, enable_cross_partition_query=True)
    #     return list(objResp);

    # def add_messages(self, messages: list[MessagesDto]) -> bool:
    #     try:
    #         for message in messages:
    #             self.container.create_item(body=message.to_dict())
    #         return True
    #     except exceptions.CosmosHttpResponseError as e:
    #         print(f"Error in DbConfig.add_messages: {str(e)}")
    #         return False