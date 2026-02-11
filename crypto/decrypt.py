from cryptography.fernet import Fernet
from config.settings import MASTER_KEY

def decrypt(token: bytes) -> str:
    return Fernet(MASTER_KEY).decrypt(token).decode()
