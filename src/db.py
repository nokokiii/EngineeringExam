import asyncio

from src.db_driver import connection as conn


class Database:    
    async def get_users(self):
        query = "SELECT * FROM Users;"
        return await conn(query)

    async def get_user(self, user_id: str):
        query = f'SELECT * FROM Users:{user_id};'
        return await conn(query)

    async def create_user(self, data: dict):
        query = (f'CREATE Users SET firstName = "{data["firstName"]}", lastName = "{data["lastName"]}", birthYear = {data["birthYear"]}, group = "{data["group"]}";')
        return await conn(query)
    
    async def update_user(self, user_id: str, is_firstname: str, is_lastname: str, is_birthyear: str, is_group: str, data: dict):
        query = f'UPDATE Users:{user_id} SET '

        if is_firstname:
            query += f'firstName = "{data["firstName"]}",'
        if is_lastname:
            query += f'lastName = "{data["lastName"]}",'
        if is_birthyear:
            query += f'birthYear = {data["birthYear"]},'
        if is_group:
            query += f'group = "{data["group"]}",'

        query = f"{query[:-1]} WHERE id = Users:{user_id};"
        return await conn(query)
    
    async def delete_user(self, user_id: str):
        query = f'DELETE FROM Users WHERE id = "{user_id}";'
        return await conn(query)
