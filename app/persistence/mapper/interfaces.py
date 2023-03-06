from abc import ABC, abstractmethod
from typing import Optional
from entities import TodoEntry


class IDatabase(ABC):
    @abstractmethod
    def connect(self, credentials:dict) -> None:
        pass

    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def create_user(self, data:dict) -> str:
        pass
    
    @abstractmethod
    def resubscribe_user(self, data:dict) -> str:
        pass
    
    @abstractmethod
    def unsubscribe_user(self, data:dict) -> str:
        pass
    
    @abstractmethod
    def update_campaign(self, data:dict) -> Optional[str]:
        pass

    @abstractmethod
    def get_subscribed_subscribers(self) -> tuple:
        pass

    @abstractmethod
    def store_email(self, content:str) -> str:
        pass

    @abstractmethod
    def create_new_campaign(self, name:str) -> str:
        pass

    @abstractmethod
    def create_new_browser(self, name:str) -> str:
        pass

    @abstractmethod
    def create_new_city(self, data:dict) -> str:
        pass

    @abstractmethod
    def create_new_country(self, name:str) -> str:
        pass

    @abstractmethod
    def create_new_os(self, name:str) -> str:
        pass

    @abstractmethod
    def load_country_id(self, name:str) -> Optional[str]:
        pass
    
    @abstractmethod
    def load_city_id(self, data:dict) -> Optional[str]:
        pass
    
    @abstractmethod
    def load_os_id(self, name:str) -> Optional[str]:
        pass

    @abstractmethod
    def load_browser_id(self, name:str) -> Optional[str]:
        pass

    @abstractmethod
    def load_single_template(self, _id:int) -> Optional[str]:
        pass

    @abstractmethod
    def load_latest_template(self, _id:int) -> Optional[str]:
        pass
    
    @abstractmethod
    def load_all_templates(self) -> Optional[str]:
        pass

    @abstractmethod
    def save_template(self, name:str, plain_data:str, html_data:str, design_data:str) -> Optional[str]:
        pass

    @abstractmethod
    def update_template(self, name:str, _id:int, plain_data:str, html_data:str, design_data:str) -> Optional[str]:
        pass

    @abstractmethod
    def delete_template(self, _id:int) -> Optional[str]:
        pass

    @abstractmethod
    def get_mapper(self) -> dict:
        """Return mapper of todo_entries"""
    
    @abstractmethod
    def create_todo(self, task:str) -> Optional[str]:
        pass

    @abstractmethod
    def get_single_todo(self, _id:int) -> Optional[str]:
        pass

    @abstractmethod
    def get_subscriber_id(self, data:dict) -> Optional[int]:
        pass

    @abstractmethod
    def get_all_campaigns(self) -> Optional[list]:
        pass

    @abstractmethod
    def email_sent(self, data:dict) -> Optional[str]:
        pass


class ICredentials(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def params() -> dict:
        pass


class Iencoder(ABC):
    @abstractmethod
    def __init__(self, credentials:bytes) -> None:
        pass

    @abstractmethod
    def encode(self, message: Optional[str | bytes | dict]) -> str:
        pass

    @abstractmethod
    def decode_to_string(self, message: Optional[str | bytes]) -> str:
        pass

    @abstractmethod
    def decode_to_json(self, message: Optional[str | bytes]) -> dict:
        pass


class IEntry_mapper(ABC):
    @abstractmethod
    async def get(self, identifier:int) -> TodoEntry:
        """Return TodoEntry entity from persistence layer"""

    @abstractmethod
    async def create(self, entity:TodoEntry) -> TodoEntry:
        """Creates new TodoEntry in persistence layer"""
