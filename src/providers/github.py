from typing import Optional

import requests

from src.exceptions.provider import ProviderErrorException
from src.schemas.user import UserOutput
from src.providers import IProvider
from src.settings import GITHUB_BASE_URL


class Github(IProvider):

    def get_user(self, username: str) -> Optional[UserOutput]:
        user = requests.get(f"{GITHUB_BASE_URL}/users/{username}")
        try:
            user.raise_for_status()
        except requests.exceptions.HTTPError:
            raise ProviderErrorException

        user = user.json()
        return UserOutput(
            id=user["id"],
            login=user["login"],
            twitter_username=user["twitter_username"],
            email=user["email"],
        )

    def __str__(self) -> str:
        return "Github"
