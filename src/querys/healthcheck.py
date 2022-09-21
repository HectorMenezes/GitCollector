from asyncpg.connection import Connection

import src.querys as querys

async def select_one(conn: Connection):
    return await querys.fetch("SELECT 1", conn)
