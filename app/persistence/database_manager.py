from typing import Optional
from persistence.mapper.interfaces import IDatabase


class Database_manager:
    def __init__(self, database:IDatabase) -> None:
        self.database = database
    
    def _create_user(self, data:dict) -> str:
        return self.database.create_user(data)
    
    def _unsubscribe_user(self, data:dict) -> str:
        return self.database.unsubscribe_user(data)
    
    def _resubscribe_user(self, data:dict) -> str:
        return self.database.resubscribe_user(data)
    
    def _create_new_campaign(self, name:str) -> str:
        return self.database.create_new_campaign(name)
    
    def _update_campaign(self, data:dict):
        return self.database.update_campaign(data)

    def _get_subscribed_subscribers(self) -> tuple:
        return self.database.get_subscribed_subscribers()

    def _create_new_browser(self, name:str) -> str:
        return self.database.create_new_browser(name)

    def _create_new_os(self, name:str) -> str:
        return self.database.create_new_os(name)

    def _create_new_country(self, name:str) -> str:
        return self.database.create_new_country(name)

    def _create_new_city(self, data:dict) -> str:
        return self.database.create_new_city(data)
    
    def _load_country_id(self, name:str) -> Optional[str]:
        return self.database.load_country_id(name)
    
    def _load_city_id(self, data:dict) -> Optional[str]:
        return self.database.load_city_id(data)
    
    def _load_email(self, email_id:int) -> Optional[str]:
        return self.database.load_email(email_id)
    
    def _load_os_id(self, name:str) -> Optional[str]:
        return self.database.load_os_id(name)
    
    def _load_browser_id(self, name:str) -> Optional[str]:
        return self.database.load_browser_id(name)
    
    def _load_single_template(self, _id:int) -> Optional[str]:
        return self.database.load_single_template(_id)
    
    def _load_latest_template(self) -> Optional[str]:
        return self.database.load_latest_template()

    def _load_all_templates(self) -> Optional[str]:
        return self.database.load_all_templates()
    
    def _save_template(self, name:str, plain_data:str, html_data:str, design_data:str) -> Optional[str]:
        return self.database.save_template(name, plain_data, html_data, design_data)
    
    def _update_template(self, name:str, _id:int, plain_data:str, html_data:str, design_data:str) -> Optional[str]:
        return self.database.update_template(name, _id, plain_data, html_data, design_data)
    
    def _delete_template(self, _id:str) -> Optional[str]:
        return self.database.delete_template(_id)

    def _get_mapper(self) -> dict:
        return self.database.get_mapper()
    
    def _create_todo(self, task:str) -> Optional[str]:
        return self.database.create_todo(task)
    
    def _get_single_todo(self, _id:int) -> Optional[str]:
        return self.database.get_single_todo(_id)
    
    def _get_subscriber_id(self, data:dict) -> str:
        return self.database.get_subscriber_id(data)
    
    def _get_campaign_id(self, name:str) -> str:
        return self.database.get_campaign_id(name)
    
    def _get_all_campaigns(self) -> list:
        return self.database.get_all_campaigns()
    
    def _email_sent(self, data:dict) -> str:
        return self.database.email_sent(data)
    