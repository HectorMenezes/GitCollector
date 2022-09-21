from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from asyncpg.connection import Connection

from src.querys.healthcheck import select_one
from src.services.database import get_conn

router = APIRouter()

@router.get("/")
def healthcheck(
    conn: Connection = Depends(get_conn)
):
    try: 
        select_one(conn)
    except Exception as error:
        return JSONResponse(
            status_code=503,
            content={
                "message": "Unable to access the database service.",
                "detais": "".join(error.args)
            }
        )
        
    return JSONResponse(
        status_code=200, content={"message": "Everything is fine!"}
    )
