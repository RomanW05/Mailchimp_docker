from cryptography.fernet import Fernet
from persistence.mapper.interfaces import Iencoder

class Encode_manager:
    def __init__(self, encoder:Iencoder) -> None:
        self.encoder = encoder
    
    def encode(self, message) -> str:
        return self.encoder.encode(message)
    
    def decode_to_json(self, message) -> dict:
        return self.encoder.decode_to_json(message)
    
    def decode_to_string(self, message) -> str:
        return self.encoder.decode_to_string(message)