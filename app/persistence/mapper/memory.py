import psycopg2

from entities import TodoEntry
from persistence.mapper.interfaces import IDatabase, IEntry_mapper
from persistence.mapper.errors import EntityNotFoundMapperError, CreateMapperError

from typing import Optional, Iterator
from contextlib import closing

from random import randint



class MysqlDatabase(IDatabase):
    def __init__(self, credentials:dict) -> None:
        self.is_connected = False
        self.credentials = credentials

    def connect(self, name: str, email: str, rollback: bool | None = None) -> object:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO subscribers (name, email) VALUES (%s,%s)''', (name, email)
            )
            if rollback == True:
                cursor.execute(
                '''SELECT FROM subscribers (name, email) WHERE name = %s AND email = %s''', (name, email)
                )
                results = cursor.fetchone()
                conn.rollback()
                return results[0]
            conn.commit()

        print(cursor, 'CURSOR')
        return cursor

        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        self.is_connected = True
        print('MySqlDatabase is active')
        connection.close()

    def create_user(self, data:dict) -> str:
        # cursor.execute(query)
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO subscribers (name, email) VALUES (%s,%s)''', (data['name'], data['email'])
            )
            conn.commit()

            # Trigger event for successful commit not implemented
        return f'New user created. Name:{data["name"]}, email:{data["email"]}'
    
    def unsubscribe_user(self, email:str):
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM subscribers WHERE email = %s''', (email,)
            )
            result = cursor.fetchone()
            if result == None:
                return 'No matchings found'
            subscriber_id = result[0]
            cursor.execute(
                '''UPDATE subscriber_status SET status = %s WHERE fk_subscriber_id = %s''',
                (False, subscriber_id)
            )
            conn.commit()
            # Trigger event for successful commit not implemented

        return f'User with id:{subscriber_id} unsubscribed'
    
    def resubscribe_user(self, email:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM subscribers WHERE email = %s''', (email,)
            )
            result = cursor.fetchone()
            if result == None:
                return 'No matchings found'
            subscriber_id = result[0]
            cursor.execute(
                '''UPDATE subscriber_status SET status = %s WHERE fk_subscriber_id = %s''',
                (True, subscriber_id)
            )
            conn.commit()

            # Trigger event for successful commit not implemented
        return f'User with id:{subscriber_id} resubscribed'
    
    def get_subscribed_subscribers(self) -> Iterator:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT subscribers.id, subscribers.email, subscribers.name
                FROM subscribers
                RIGHT JOIN subscriber_status
                ON subscriber_status.fk_subscriber_id = subscribers.id
                WHERE subscriber_status.status = True'''
            )
            for subscribed in cursor.fetchall():
                yield subscribed
    
    def store_email(self, content:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO emails (content) VALUES (%s)''', (content,)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'Email archived'

    def create_new_campaign(self, name:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO campaign (name) VALUES (%s)''', (name,)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'New campaign created'
    
    def update_campaign(self, data:dict) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO campaign_status (fk_subscriber_id, fk_campaign_id, section, fk_os_id, fk_browser_id, fk_country_id, fk_city_id, ip)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',
                (data['fk_subscriber_id'],data['fk_campaign_id'],data['section'],data['fk_os_id'],data['fk_browser_id'],data['fk_country_id'],data['fk_city_id'],data['ip'])
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'Campaign archived'

    def create_new_os(self, name:str) -> str:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO os (name) VALUES (%s)''', (name,)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'os archived'
    
    def create_new_browser(self, name:str) -> str:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO browsers (name) VALUES (%s)''', (name,)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'browser archived'

    def create_new_country(self, name:str) -> str:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO countries (name) VALUES (%s)''', (name,)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'country archived'
    
    def create_new_city(self, data:dict) -> str:
        country_id = self.load_country_id(data['country'])
        if country_id is None:
            self.create_new_country(data['country'])
            country_id = self.load_country_id(data['country'])

        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO cities (name, fk_country_id) VALUES (%s, %s)''', (data['city'], country_id)
            )
            conn.commit()
        # Trigger event for successful commit not implemented
        return 'city archived'

    def load_country_id(self, name:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM countries WHERE name = %s''', (name,)
            )
            result = cursor.fetchone()
            if result == None:
                cursor.execute(
                '''INSERT INTO countries (name) VALUES (%s)''', (name,)
                )
                conn.commit()
                cursor.execute(
                '''SELECT CURRVAL(
                pg_get_serial_sequence('countries', 'id'))'''
                )
                result = cursor.fetchone()
                return result[0]

        return result[0]
    
    def load_city_id(self, data:dict) -> Optional[dict]:
        country_id = self.load_country_id(data['country'])
        city = data['city']
        if country_id is None:
            return None
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM cities WHERE fk_country_id = %s AND name = %s''', (country_id, city)
            )
            result = cursor.fetchone()
            if result == None:
                cursor.execute(
                '''INSERT INTO cities (fk_country_id, name) VALUES (%s,%s)''', (country_id, city)
                )
                conn.commit()
                cursor.execute(
                '''SELECT CURRVAL(
                pg_get_serial_sequence('cities', 'id'))'''
                )
                result = cursor.fetchone()
                return result[0]

        return {'city_id':result[0], 'country_id':country_id}
        
    def load_os_id(self, name:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            
            cursor.execute(
                '''SELECT id FROM os WHERE name = %s''', (name,)
            )
            result = cursor.fetchone()
            if result == None:
                cursor.execute(
                '''INSERT INTO os (name) VALUES (%s)''', (name,)
                )
                conn.commit()
                cursor.execute(
                '''SELECT CURRVAL(
                pg_get_serial_sequence('os', 'id'))'''
                )
                result = cursor.fetchone()
                return result[0]

        return result[0]

    def load_browser_id(self, name:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM browsers WHERE name = %s''', (name,)
            )
            result = cursor.fetchone()
            if result == None:

                cursor.execute(
                '''INSERT INTO browsers (name) VALUES (%s)''', (name,)
                )
                conn.commit()
                cursor.execute(
                '''SELECT CURRVAL(
                pg_get_serial_sequence('browsers', 'id'))'''
                )
                result = cursor.fetchone()
                return result[0]

        return result[0]
    
    def load_single_template(self, _id:int) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id, name, plain_data, html_data, design_data FROM templates WHERE id = %s''', (_id,)
            )
            result = cursor.fetchone()
            if result == None:
                return None

        return result
    
    def load_latest_template(self) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id, name, plain_data, html_data, design_data FROM templates WHERE id = (SELECT MAX(id) FROM templates)'''
            )
            result = cursor.fetchone()
            if result == None:
                return None

        return result
    
    def load_all_templates(self) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id, name FROM templates'''
            )
            result = cursor.fetchall()
            if result == None:
                return None

        return result
    
    def save_template(self, name:str, plain_data:str, html_data:str, design_data:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO templates (name, plain_data, html_data, design_data) VALUES (%s, %s, %s, %s)''',
                (name, plain_data, html_data, design_data)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'ok'
    
    def update_template(self, name:str, _id:int, plain_data:str, html_data:str, design_data:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''UPDATE templates SET name = %s, plain_data = %s, html_data = %s, design_data = %s WHERE id = %s''',
                (name, plain_data, html_data, design_data, _id)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'ok'
    
    def delete_template(self, _id:int) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''DELETE FROM templates WHERE id = %s''', (_id,)
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'ok'
    
    def get_mapper(self) -> dict:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT * FROM todo'''
            )
            result = cursor.fetchall()
            return result
        
            mapper = {}
            for i, row in enumerate(result):
                mapper[i] = dict(zip(['id', 'task'], row))

            if result == None:
                return None
        return mapper
    

    def create_todo(self, task:str) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO todo (task) VALUES (%s)''', (task,)
            )
            conn.commit()
        # Trigger event for successful commit not implemented
        return 'todo created'
    
    def get_single_todo(self, _id:int) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT task FROM todo WHERE id = %s''', (_id,)
            )
            result = cursor.fetchone()
            if result == None:
                return None
            # Trigger event for successful commit not implemented

        return result
    
    def get_subscriber_id(self, data) -> dict:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM subscribers WHERE name = %s AND email = %s''',
                (data['name'], data['email'])
            )
            result = cursor.fetchone()
            return result[0]
        
    def get_campaign_id(self, name) -> int:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id FROM campaign WHERE name = %s''', (name,)
            )
            result = cursor.fetchone()
            if result is not None:
                return result[0]
        return None
    
    def get_all_campaigns(self) -> str:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT id, name FROM campaign'''
            )
            result = cursor.fetchall()
            if result is not None:
                return result
        return []
    
    def email_sent(self, data: dict) -> Optional[str]:
        with closing(psycopg2.connect(**self.credentials)) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO sent_emails (fk_campaign_id, fk_subscriber_id, fk_template_id, status, hashed) VALUES (%s,%s,%s,%s,%s) ''',
                           (data['campaign_id'], data['subscriber_id'], data['template_id'], data['status'], data['hashed'])
            )
            conn.commit()
            # Trigger event for successful commit not implemented
        return 'ok'

        

        # _MAPPER_IN_MEMORY_STORAGE = {
        #     1:TodoEntry(id=1, summary="Lorem Ipsum"),
        #     2:TodoEntry(id=2, summary="Lorem Ipsum"),
        #     3:TodoEntry(id=3, summary="Lorem Ipsum"),
        #     4:TodoEntry(id=4, summary="Lorem Ipsum"),
        #     5:TodoEntry(id=5, summary="Lorem Ipsum"),
        #     6:TodoEntry(id=6, summary="Lorem Ipsum"),
        #     7:TodoEntry(id=7, summary="Lorem Ipsum"),
        #     8:TodoEntry(id=8, summary="Lorem Ipsum")
        # }
        # return _MAPPER_IN_MEMORY_STORAGE
        

        # with closing(psycopg2.connect(**self.credentials)) as conn:
        #     cursor = conn.cursor()
        #     cursor.execute(
        #         '''SELECT * FROM mapper'''
        #     )
        #     result = cursor.fetchone()
        #     if result == None:
        #         return {id:0}
        #     else:
        #         return result[0]

    def close(self) -> None:
        print('db closed')
    

class MemoryTodoEntryMapper(IEntry_mapper):
    _storage:dict

    def __init__(self, storage:dict) -> None:
        self._storage = storage

    async def get(self, identifier:int) -> TodoEntry:
        try:
            return self._storage[identifier]
        except KeyError:
            raise EntityNotFoundMapperError(f"Entity `id:{identifier}` was not found.")

    async def create(self, entity:TodoEntry) -> TodoEntry:
        try:
            entity.id = self._generate_unique_id()
            self._storage[entity.id] = entity
            return entity
        except TypeError as error:
            raise CreateMapperError(error)

    def _generate_unique_id(self) -> int:
        identifier = randint(1, 10_000)
        while identifier in self._storage:
            identifier = randint(1, 10_000)

        return identifier