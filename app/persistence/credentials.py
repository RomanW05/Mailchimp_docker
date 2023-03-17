from config import config, encoder
from abc import ABC, abstractmethod


class Credentials(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def params() -> dict:
        pass


class Encoder_credentials_from_file(Credentials):
    def __init__(self) -> None:
        self.params_encoder = encoder()
    
    def params(self) -> bytes:
        self.params_encode = self.params_encoder['encoder_key'].encode()
        return self.params_encode


class Encoder_credentials_from_input(Credentials):
    def __init__(self) -> None:
        self.params_encoder = {
            'encoder_key' : input('Please, enter your encoder password: '),
        }

    def params(self) -> bytes:
        self.params_encoder = self.params_encoder.encode()
        return self.params_encoder
    


class Credentials_from_file(Credentials):
    def __init__(self) -> None:
        self.params_db = config()
    
    def params(self) -> dict:
        return self.params_db


class Credentials_from_input(Credentials):
    def __init__(self) -> None:
        self.params_db = {
            'host' : input('Please, enter your database host address: '),
            'database' : input('Please, enter your database name: '),
            'user' : input('Please, enter your database user: '),
            'password' : input('Please, enter your database password: '),
            'encoder_key' : input('Please, enter your encoder password: '),
        }

    def params(self):
        return self.params_db