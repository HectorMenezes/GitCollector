from asyncpg.connection import Connection

from src.querys import insert
from src.schemas.user import UserOutput
from src.providers.provider import ProviderType


async def insert_user(user: UserOutput, provider: ProviderType, conn: Connection):
    return await insert(
        table="user",
        columns=["login", "email", "twitter_username", "provider"],
        values=[user.login, user.email, user.twitter_username, provider.value],
        conn=conn,
    )
