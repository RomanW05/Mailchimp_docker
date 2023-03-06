from config import config
from persistence.mapper.interfaces import Credentials

class ICredentials_from_file(Credentials):
    def __init__(self) -> None:
        self.params_db = config()
    
    def params(self) -> dict:
        return self.params_db


class ICredentials_from_input(Credentials):
    def __init__(self) -> None:
        self.params_db = {
            'host' : input('Please, enter your host address: '),
            'database' : input('Please, enter your database name: '),
            'user' : input('Please, enter your user: '),
            'password' : input('Please, enter your password: ')
        }

    def params(self):
        return self.params_db