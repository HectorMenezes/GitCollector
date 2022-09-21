from typing import Any, List
from asyncpg.connection import Connection


async def fetch(statement: str, conn: Connection):
    async with conn as connection:
        async with connection.transaction():
            await connection.fetch(statement)


async def insert(table: str, columns: List[str], values: List[Any], conn: Connection):
    async with conn as connection:
        async with connection.transaction():
            columns = ",".join(columns)

            value_positions = ",".join([f"${i + 1}" for i in range(len(values))])

            query = f"""
                INSERT INTO \"{table}\"({columns})
                VALUES ({value_positions})
            """
            return await connection.execute(query, *values)
