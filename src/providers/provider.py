from typing import Optional
from enum import Enum

from src.providers import BaseProvider
from src.providers.github import Github
from src.providers.gitlab import Gitlab
from src.schemas.user import UserOutput

class ProviderType(Enum):
    GITHUB = "Github"
    GITLAB = "Gitlab"


class Provider(BaseProvider):
    def __init__(self, provider: BaseProvider) -> None:
        self.provider: BaseProvider = {
            "Github": Github,
            "Gitlab": Gitlab
        }.get(provider)()
    
    def get_user(self, username: str) -> Optional[UserOutput]:
        return self.provider.get_user(username=username)
