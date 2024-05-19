from typing import Generic, TypeVar
from enum import Enum

# Define an Enum for status
class StatusEnum(Enum):
    OK = 200
    ERROR = 500
    # Add more status values as needed

T = TypeVar('T')

class GenResponse(Generic[T]):
    def __init__(self, data: T, message: str, status: StatusEnum = StatusEnum.OK):
        self.status = status
        self.message = message
        self.data = data

    @classmethod
    def success(cls, data: T, message: str, status: StatusEnum = StatusEnum.OK) -> 'GenResponse[T]':
        return cls(data=data, message=message, status=status)