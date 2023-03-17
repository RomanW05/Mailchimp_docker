import json
from cryptography.fernet import Fernet
from persistence.mapper.interfaces import Iencoder




class Encoder(Iencoder):
    def __init__(self, credentials:bytes) -> None:
        self.cifer = Fernet(credentials)

    @staticmethod
    def create_new_key():
        key = Fernet.generate_key()
        return key
    
    def encode(self, message: str | bytes | dict) -> str:
        if type(message) == str:
            message = message.encode()
        elif type(message) == dict:
            message = json.dumps(message)
            message = message.encode()
        bytes_params = self.cifer.encrypt(message)
        str_params = bytes_params.decode('utf-8')
        return str_params

    def decode_to_json(self, message: str | bytes) -> dict:
        if type(message) != bytes:
            message = message.encode()
        bytes_params = self.cifer.decrypt(message)
        str_params = bytes_params.decode('utf-8')
        json_params = json.loads(str_params)
        return json_params
    
    def decode_to_string(self, message: str | bytes | dict) -> str:
        if type(message) != bytes:
            message = message.encode()
        bytes_params = self.cifer.decrypt(message)
        str_params = bytes_params.decode('utf-8')
        return str_params
    
