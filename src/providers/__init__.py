from abc import ABC, abstractmethod
from typing import Optional

from src.schemas.user import UserOutput
from src.exceptions.provider import NotImplementedException

class BaseProvider(ABC):

    @abstractmethod
    def get_user(self, username: str) -> Optional[UserOutput]:
        raise NotImplementedException
