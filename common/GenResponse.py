from typing import Generic, Optional, TypeVar
from enum import Enum
from pydantic import BaseModel

# Define the StatusCodeEnum
class StatusCodeEnum(Enum):
    OK = 200
    BadRequest = 400
    # Add other status codes as needed

# Define the GenResponse class inheriting from BaseModel
T = TypeVar('T')

class GenResponse(BaseModel, Generic[T]):
    is_success: bool = False
    data: Optional[T] = None
    message: Optional[str] = None
    error: Optional[str] = None
    stat_code: int = StatusCodeEnum.OK.value

    @staticmethod
    def success(data: T, status_code: StatusCodeEnum = StatusCodeEnum.OK, message: Optional[str] = None) -> 'GenResponse[T]':
        return GenResponse(is_success=True, data=data, message=message, stat_code=status_code.value)

    @staticmethod
    def failed(error: str, status_code: StatusCodeEnum = StatusCodeEnum.BadRequest) -> 'GenResponse[None]':
        return GenResponse(is_success=False, error=error, stat_code=status_code.value)
