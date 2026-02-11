from cryptography.fernet import Fernet
from config.settings import MASTER_KEY

def encrypt(text: str) -> bytes:
    return Fernet(MASTER_KEY).encrypt(text.encode())
