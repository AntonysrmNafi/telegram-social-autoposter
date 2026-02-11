import os
from crypto.encrypt import encrypt
from crypto.decrypt import decrypt

TOKEN_PATH = "storage/tokens"

def token_file(user_id):
    return f"{TOKEN_PATH}/x_{user_id}.enc"

def is_x_connected(user_id):
    return os.path.exists(token_file(user_id))

def remove_x_token(user_id):
    try:
        os.remove(token_file(user_id))
    except:
        pass

def get_x_auth_url(user_id):
    return f"https://api.twitter.com/oauth/authorize?state={user_id}"
