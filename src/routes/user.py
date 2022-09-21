from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from asyncpg.connection import Connection

from src.providers.provider import Provider, ProviderType
from src.schemas.user import UserOutput
from src.services.database import get_conn
from src.querys.user import insert_user
import src.docs.user as user_docs
from src.exceptions.provider import ProviderErrorException

router = APIRouter()

@router.get(
    "/{username}",
    response_model=UserOutput,
    **user_docs.get_by_username
)
async def get_user(
    username: str,
    provider_type: ProviderType,
    max_lag_day: int = 15,
    conn: Connection = Depends(get_conn)
):
    provider = Provider(provider_type.value)
    try:
        user = provider.get_user(username=username)
        await insert_user(user=user, provider=provider_type, conn=conn)
        return user
    except ProviderErrorException as error:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Provider {provider_type.name} returned an error.",
                "details": "".join(error.args)
            }
        )

