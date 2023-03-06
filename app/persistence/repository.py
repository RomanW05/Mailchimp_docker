from typing import Optional

from persistence.credentials import Credentials_from_file, Credentials_from_input
from persistence.mapper.memory import MysqlDatabase
from persistence.mapper.interfaces import IDatabase



class Database_manager:
    def __init__(self, database: IDatabase) -> None:
        self.database = database
    
    def _create_user(self, data: dict) -> str:
        return self.database.create_user(data)
    
    def _unsubscribe_user(self, data: dict) -> str:
        return self.database.unsubscribe_user(data)
    
    def _resubscribe_user(self, data: dict) -> str:
        return self.database.resubscribe_user(data)
    
    def _create_new_campaign(self, name: str) -> str:
        return self.database.create_new_campaign(name)
    
    def _update_campaign(self, data: dict):
        return self.database.update_campaign(data)

    def _get_subscribed_subscribers(self) -> tuple:
        return self.database.get_subscribed_subscribers()
    
    def _store_email(self, content: str) -> str:
        return self.database.store_email(content)

    def _create_new_browser(self, name: str) -> str:
        return self.database.create_new_browser(name)

    def _create_new_os(self, name: str) -> str:
        return self.database.create_new_os(name)

    def _create_new_country(self, name: str) -> str:
        return self.database.create_new_country(name)

    def _create_new_city(self, data: dict) -> str:
        return self.database.create_new_city(data)
    
    def _load_country_id(self, name: str) -> Optional[str]:
        return self.database.load_country_id(name)
    
    def _load_city_id(self, data: dict) -> Optional[str]:
        return self.database.load_city_id(data)
    
    def _load_email(self, email_id: int) -> Optional[str]:
        return self.database.load_email(email_id)
    
    def _load_os_id(self, name: str) -> Optional[str]:
        return self.database.load_os_id(name)
    
    def _load_browser_id(self, name: str) -> Optional[str]:
        return self.database.load_browser_id(name)

    def _get_mapper(self) -> dict:
        return self.database.get_mapper()


        


def factory():
    # data = {
    #     'fk_subscriber_id': 3,
    #     'fk_newsletter_campaign_id': 1,
    #     'section': 1,
    #     'fk_os_id': 1,
    #     'fk_browser_id': 1,
    #     'fk_country_id': 1,
    #     'fk_city_id': 1,
    # }
    credentials = Credentials_from_file()
    database = MysqlDatabase(credentials.params())
    db = Database_manager(database=database)
    # db._create_user({'name':'user1', 'email':'a1asd@asd.com'})
    # db._unsubscribe_user('a1asd@asd.com')
    # db._resubscribe_user('a1asd@asd.com')
    # for elem in db._get_subscribed_subscribers():
    #     print(elem)
    # db._store_email('''Dear XXX,\nthank you\nCOMPANY NAME''')
    # print(db._load_email(1))
    # db._create_new_campaign('campaign1')
    # db._update_campaign(data)
    # db._create_new_browser('Firefox 10.0')
    # db._create_new_os('Windows 10')
    # db._create_new_country('Brazil')
    # db._create_new_city({'name': 'city1', 'fk_country_id': 1})
    # print(db._load_country_id('Brazil'))
    # print(db._load_city_id({'country':'Brazil', 'city':'city1'}))
    # print(db._load_os_id('Windows 10'))
    # print(db._load_browser_id('Firefox 10.0'))
    

    return db

factory()