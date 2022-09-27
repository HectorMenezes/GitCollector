from enum import Enum

from src.providers.provider import PROVIDER_MAPPING

ProviderType = Enum("ProviderType", {key: str(value()) for key, value in PROVIDER_MAPPING.items()})
