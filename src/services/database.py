import asyncpg
from asyncpg.pool import Pool

from src.settings import DB_CONNECTION_STRING

CONNECTION_POOL: Pool = None

async def init_pool():
    global CONNECTION_POOL
    CONNECTION_POOL = await asyncpg.create_pool(dsn=DB_CONNECTION_STRING)

def get_conn():
    return CONNECTION_POOL.acquire()
