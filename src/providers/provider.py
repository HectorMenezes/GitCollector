from typing import Optional
from enum import Enum

from src.providers import IProvider
from src.providers.github import Github
from src.providers.gitlab import Gitlab
from src.schemas.user import UserOutput

PROVIDER_MAPPING = {
    "Github": Github,
    "Gitlab": Gitlab
}

class Provider(IProvider):
    def __init__(self, provider: IProvider) -> None:
        self.provider: IProvider = PROVIDER_MAPPING.get(provider)()
    
    def get_user(self, username: str) -> Optional[UserOutput]:
        return self.provider.get_user(username=username)
